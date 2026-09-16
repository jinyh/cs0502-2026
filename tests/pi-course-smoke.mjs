// Pi 0.85.1 课程兼容性试测；不安装依赖、不修改个人配置、不启动子智能体。
// PI_PACKAGE_DIR=<Pi npm 包目录> node tests/pi-course-smoke.mjs [--live]
// 默认检查仓库内 Pi 适配层、共享资源加载与路径护栏；--live 使用本机 Pi 默认模型与凭据产生真实 API 调用。
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, realpathSync, rmSync, writeFileSync } from "node:fs";
import { homedir, tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const packageDir = process.env.PI_PACKAGE_DIR;
if (!packageDir) throw new Error("请通过 PI_PACKAGE_DIR 指定已安装 Pi 的 npm 包目录。");
const sdk = await import(pathToFileURL(path.join(packageDir, "dist/index.js")));
const { AuthStorage } = await import(pathToFileURL(path.join(packageDir, "dist/core/auth-storage.js")));
const { expandPromptTemplate } = await import(pathToFileURL(path.join(packageDir, "dist/core/prompt-templates.js")));
const scratch = mkdtempSync(path.join(tmpdir(), "cs0502-pi-smoke-"));
const cwd = path.join(scratch, "course");
const agentDir = path.join(scratch, "agent");
mkdirSync(cwd);
mkdirSync(agentDir);

// 复制 Git 已跟踪或待提交且未被忽略的公开课程文本，原仓库和个人目录不暴露给模型工具。
const files = execFileSync("git", ["ls-files", "--cached", "--others", "--exclude-standard", "-z"], {
  cwd: root,
  encoding: "utf8",
}).split("\0");
for (const name of files) {
  if (!/^(docs\/|opencode\/|\.opencode\/|\.pi\/|code\/)/.test(name) && name !== "AGENTS.md") continue;
  if (!/\.(md|json|jsonl|yaml|py|ts)$/.test(name)) continue;
  const source = path.join(root, name);
  if (realpathSync(source) !== source) throw new Error("试测不复制符号链接。");
  mkdirSync(path.dirname(path.join(cwd, name)), { recursive: true });
  cpSync(source, path.join(cwd, name));
}

const allowedTools = ["read", "grep", "find", "ls"];
const adapterPath = path.join(cwd, ".pi/extensions/course-tutor.ts");
const adapter = await import(pathToFileURL(adapterPath));
const checkCall = (name, input) => adapter.checkCourseToolCall(name, input, cwd);
const projectSettings = JSON.parse(readFileSync(path.join(cwd, ".pi/settings.json"), "utf8"));
assert.deepEqual(projectSettings.defaultTools, allowedTools);

const settingsManager = sdk.SettingsManager.inMemory({
  defaultProjectTrust: "never",
  retry: { enabled: false, provider: { maxRetries: 0, timeoutMs: 90000 } },
});
const common = { cwd, agentDir, settingsManager, noExtensions: true, noThemes: true };
const report = {
  piVersion: JSON.parse(readFileSync(path.join(packageDir, "package.json"), "utf8")).version,
  mode: process.argv.includes("--live") ? "live" : "offline",
  results: [],
};

try {
  const bare = new sdk.DefaultResourceLoader(common);
  await bare.reload();
  const courseSkillNames = ["guided-learning", "assessment-practice", "code-lab-coach", "retrieval-review", "frontier-literacy"];
  report.bare = {
    courseSkills: bare.getSkills().skills.filter(s => courseSkillNames.includes(s.name)).length,
    otherSkills: bare.getSkills().skills.filter(s => !courseSkillNames.includes(s.name)).length,
    courseCommands: bare.getPrompts().prompts.length,
    contextFiles: bare.getAgentsFiles().agentsFiles.map(f => path.relative(cwd, f.path)),
  };
  assert.equal(report.bare.courseSkills, 0);
  assert.equal(report.bare.courseCommands, 0);

  const loader = new sdk.DefaultResourceLoader({
    ...common,
    noContextFiles: true,
    additionalExtensionPaths: [adapterPath],
    // ResourceLoader 单独使用时不会触发会话级 resources_discover；显式加入同一维护源验证内容。
    additionalSkillPaths: [path.join(cwd, ".opencode/skills")],
    additionalPromptTemplatePaths: [path.join(cwd, ".opencode/commands")],
  });
  await loader.reload();
  const loadedSkills = loader.getSkills().skills;
  report.adapted = {
    skills: loadedSkills.filter(s => courseSkillNames.includes(s.name)).map(s => s.name),
    otherSkills: loadedSkills.filter(s => !courseSkillNames.includes(s.name)).map(s => s.name),
    commands: loader.getPrompts().prompts.map(p => p.name),
    diagnostics: [...loader.getSkills().diagnostics, ...loader.getPrompts().diagnostics].map(d => d.message),
    contextFiles: loader.getAgentsFiles().agentsFiles.length,
    extensions: loader.getExtensions().extensions.length,
    extensionErrors: loader.getExtensions().errors.length,
  };
  assert.deepEqual(new Set(report.adapted.skills), new Set(courseSkillNames));
  assert.equal(report.adapted.commands.length, 10);
  assert.equal(report.adapted.contextFiles, 0);
  assert.equal(report.adapted.extensions, 1);
  assert.equal(report.adapted.extensionErrors, 0);
  assert.equal(report.adapted.diagnostics.length, 0);
  for (const template of loader.getPrompts().prompts) {
    const expanded = expandPromptTemplate(`/${template.name} L05 图遍历`, loader.getPrompts().prompts);
    assert.ok(expanded.includes("L05 图遍历"));
    assert.ok(!expanded.includes("$ARGUMENTS"));
    assert.ok(!expanded.includes("agent: course-tutor"));
  }
  report.templateChecks = 10;
  for (const [name, input] of [
    ["bash", { command: "ls" }], ["write", { path: "student-work/test.md" }],
    ["read", { path: "reference/fake.md" }], ["read", { path: "../outside.md" }],
    ["read", { path: ".env" }], ["grep", { path: homedir() }],
  ]) assert.equal(checkCall(name, input)?.block, true);
  assert.equal(checkCall("read", { path: "opencode/knowledge.md" }), undefined);
  report.guardChecks = 7;
  console.log(JSON.stringify({ phase: "resources", ...report }));

  if (process.argv.includes("--live")) {
    const userDir = path.join(homedir(), ".pi/agent");
    const userSettings = JSON.parse(readFileSync(path.join(userDir, "settings.json"), "utf8"));
    const credentials = AuthStorage.inMemory(JSON.parse(readFileSync(path.join(userDir, "auth.json"), "utf8")));
    const runtime = await sdk.ModelRuntime.create({
      credentials, modelsPath: path.join(userDir, "models.json"),
      modelsStorePath: path.join(agentDir, "models-cache.json"), allowModelNetwork: false,
    });
    const model = runtime.getModel(userSettings.defaultProvider, userSettings.defaultModel);
    assert.ok(model, "本机 Pi 默认模型不可用。");
    report.model = model.id;
    report.thinking = "off";
    const cases = [
      ["start", "/start L06。我不启用学习记录。"],
      ["learn", "/learn L15"],
      ["demo", "/demo L05 图遍历"],
      ["lab", "/lab lab-02-graph"],
    ];
    for (const [name, prompt] of cases) {
      const began = performance.now();
      const { session } = await sdk.createAgentSession({
        cwd, agentDir, modelRuntime: runtime, model, thinkingLevel: "off",
        settingsManager, resourceLoader: loader, tools: allowedTools,
        sessionManager: sdk.SessionManager.inMemory(cwd),
      });
      const result = { name, firstTextSeconds: null, totalSeconds: null, tools: [], text: "", stopReasons: [] };
      session.subscribe(event => {
        if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
          result.firstTextSeconds ??= (performance.now() - began) / 1000;
          result.text += event.assistantMessageEvent.delta;
        }
        if (event.type === "tool_execution_start") result.tools.push({ name: event.toolName, args: event.args });
        if (event.type === "message_end" && event.message.role === "assistant") {
          result.stopReasons.push(event.message.stopReason);
          // 外部服务的原始错误可能回显配置；报告只保留错误类别。
          if (event.message.errorMessage) result.error = /connect|network|fetch|timeout/i.test(event.message.errorMessage)
            ? "connection-error" : "provider-error";
        }
      });
      const timer = setTimeout(() => { void session.abort(); }, 120000);
      try {
        await session.prompt(prompt, { expandPromptTemplates: true });
        result.totalSeconds = (performance.now() - began) / 1000;
        result.completed = result.stopReasons.at(-1) === "stop";
        result.noProgressWritten = !existsSync(path.join(cwd, "student-work/progress.json"));
        report.results.push(result);
        console.log(JSON.stringify({ phase: "case", ...result }));
      } finally {
        clearTimeout(timer);
        session.dispose();
      }
      // 连接或认证失败时结束，不把失败请求记成速度结果，也不重复相同请求。
      if (!result.completed) break;
    }
  }
  const output = process.env.PI_SMOKE_REPORT;
  if (output) writeFileSync(output, JSON.stringify(report, null, 2) + "\n");
  if (report.mode === "live" && report.results.some(result => !result.completed)) process.exitCode = 1;
} finally {
  rmSync(scratch, { recursive: true, force: true });
}
