# Pi 课程兼容性试测

> 教师验收入口。仓库已经提供只读学生试用配置；本脚本验证 Pi 0.85.1 与 macOS，升级后应重新检查兼容性。

## 本地资源检查

前置条件：Git checkout、Node.js、已安装的 Pi npm 包。不需要安装本项目的 Node.js 依赖。

在仓库根目录运行，`PI_PACKAGE_DIR` 指向实际安装位置：

```bash
export PI_PACKAGE_DIR="$(npm root -g)/@earendil-works/pi-coding-agent"
node tests/pi-course-smoke.mjs
```

检查项目信任前后的资源差异、仓库 `.pi` 适配层、5 个 skills、10 个命令及参数展开、7 项路径护栏。脚本只复制 Git 已跟踪或待提交且未被忽略的公开课程文本到临时目录，结束时清理；不会修改原仓库的课程资源或个人 Agent 配置。

## 真实模型调用

教师先在本机 Pi 中配置模型并确认可以使用。脚本从 Pi 用户目录读取默认模型设置和模型定义，凭据只放入进程内存，不打印、不复制到临时目录。该调用会将公开课程内容与测试提示发送到教师已配置的模型服务并产生 API 用量。

```bash
node tests/pi-course-smoke.mjs --live
```

可通过 `PI_SMOKE_REPORT` 指定本地 JSON 报告路径；报告含生成回复与工具轨迹，请审核后再引用。每个场景使用新会话，推理设置为 `off`，最多等待 120 秒；连接失败会停止后续场景并返回非零状态。

按以下标准人工检查回复与工具轨迹，不能只凭脚本退出码认定教学验收通过：

| 场景 | 应看到的行为 |
|---|---|
| `/start L06。我不启用学习记录。` | 尊重拒绝，不写文件；不预读完整索引/映射；提出一道诊断题 |
| `/learn L15` | 按课程映射选择 `probability-uncertainty`，不能错用同编号可视化卡；先提出诊断或预测问题 |
| `/demo L05 图遍历` | 用运行索引定位 `06_graph_bfs_dfs.py`，先预测；不在本机运行代码 |
| `/lab lab-02-graph` | 查公开 Lab 资料和计分关联；先预测，给云端 helper，不声称代码已经运行 |

## 试测边界

- `.pi/settings.json` 只开放 `read/grep/find/ls`，项目扩展把 Pi 的 `find/ls` 对应到共享规则中的 `glob/list`。
- 不开放进度写入、联网检索、通用 shell 或代码执行；模型应明确说明缺失能力。
- 项目扩展复用助教提示正文，但不继承 OpenCode 的 `permission:` 配置；工具和路径限制由 Pi 扩展独立执行。
- 临时目录只含公开资料；测试调用与学生试用入口使用同一份路径检查函数。
- 首字时间可能是模型开始说明行动的时间。判断学习体验时，同时检查整轮时间、检索轮数和最终问题是否合格。

项目兼容性状态见[学习智能体兼容性](../docs/agent-compatibility.md)。OpenCode 的原有入口与[验收场景](manual-opencode-smoke.md)继续保留。
