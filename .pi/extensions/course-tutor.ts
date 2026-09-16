import { existsSync, readFileSync, realpathSync } from "node:fs";
import { dirname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";

const extensionDir = dirname(fileURLToPath(import.meta.url));
const courseRoot = realpathSync(resolve(extensionDir, "../.."));
const tutorFile = join(courseRoot, ".opencode/agents/course-tutor.md");
const skillsDir = join(courseRoot, ".opencode/skills");
const promptsDir = join(courseRoot, ".opencode/commands");

const allowedTools = new Set(["read", "grep", "find", "ls"]);
const allowedRoots = [
  ".opencode",
  "opencode",
  "docs",
  "code",
  "figures",
  "notebooks/modelscope",
  "student-work",
];
const allowedRootFiles = new Set(["README.md", "LICENSE"]);

function stripFrontmatter(text: string): string {
  return text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "").trim();
}

function resolveThroughExistingAncestor(target: string): string {
  let existing = target;
  while (!existsSync(existing)) {
    const parent = dirname(existing);
    if (parent === existing) return target;
    existing = parent;
  }
  return resolve(realpathSync(existing), relative(existing, target));
}

function normalizedRelativePath(cwd: string, requestedPath: string): string | undefined {
  const target = resolveThroughExistingAncestor(resolve(cwd, requestedPath));
  const rel = relative(courseRoot, target);
  if (!rel || rel === "." || rel.startsWith(`..${sep}`) || rel === "..") return undefined;
  return rel.split(sep).join("/");
}

export function checkCourseToolCall(
  toolName: string,
  input: Record<string, unknown>,
  cwd: string = courseRoot,
): { block: true; reason: string } | undefined {
  if (!allowedTools.has(toolName)) {
    return { block: true, reason: "Pi 课程入口只开放只读课程检索工具。" };
  }

  const requestedPath = typeof input.path === "string" ? input.path : "";
  if (!requestedPath) {
    return { block: true, reason: "请为检索指定一个课程公开目录。" };
  }

  const rel = normalizedRelativePath(cwd, requestedPath);
  if (!rel) {
    return { block: true, reason: "Pi 课程入口不允许读取仓库根目录或课程目录之外的路径。" };
  }

  const allowed = allowedRootFiles.has(rel)
    || allowedRoots.some((root) => rel === root || rel.startsWith(`${root}/`));
  const sensitive = /(^|\/)(reference|LectureNotes|\.git)(\/|$)/.test(rel)
    || /(^|\/)\.env(?:\.|$)/.test(rel)
    || /(?:^|\/)\w*secret\w*(?:\.|$)/i.test(rel);

  if (!allowed || sensitive) {
    return { block: true, reason: `路径“${rel}”不属于 Pi 课程入口允许读取的公开资源。` };
  }
  return undefined;
}

const tutorRules = stripFrontmatter(readFileSync(tutorFile, "utf8"));
const piAdapter = `
## Pi 课程适配

- 上述正文是 OpenCode 与 Pi 共用的课程助教规则；其中 OpenCode 专用的 frontmatter 权限没有注入 Pi。
- Pi 中用 find 对应 OpenCode 的 glob，用 ls 对应 OpenCode 的 list；read 与 grep 含义相同。
- 当前 Pi 课程入口只开放课程范围内的只读检索，不提供 shell、写入、联网或本机代码执行。需要这些能力时明确说明当前限制，继续完成可以只读进行的学习步骤；不得声称已经保存进度、写入笔记、联网或运行代码。
- example、Lab 与可视化仍在学生自己的 PAI-DSW 中运行，通过 [CS0502_RESULT] 摘要手动交接。
`;

export default function courseTutorExtension(pi: ExtensionAPI) {
  pi.on("resources_discover", () => ({
    skillPaths: [skillsDir],
    promptPaths: [promptsDir],
  }));

  pi.on("before_agent_start", (event) => ({
    systemPrompt: `${event.systemPrompt}\n\n${tutorRules}\n\n${piAdapter}`,
  }));

  pi.on("tool_call", (event, ctx) => {
    return checkCourseToolCall(event.toolName, event.input as Record<string, unknown>, ctx.cwd);
  });
}
