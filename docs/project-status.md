# 项目进度记录

> 2026-09-08 从根级 `AGENTS.md` 迁入；资源数量和完成状态为原有记录，未在本次配置整理中重新审计。后续更新在本文件集中维护。

## 当前进度

### 2026-09-16 智能体兼容性验证

- 保留现有 OpenCode 完整课程入口；Pi 通过 `.pi/` 薄适配层复用同一套教学 skills、命令和助教规则，不复制内容。
- 网站总入口统一为“AI 助学”，分别提供 OpenCode 指南与 Pi 只读试用指南；2026 版 Slide01/02 已同步使用通用助教表述。
- Pi 0.85.1 已通过项目资源加载、10 个命令参数展开和工具路径护栏检查；只读学生试用入口已加入仓库。
- Pi 的真实教学回复、速度对比、进度写入和联网权限仍待验证。详见[学习智能体兼容性](agent-compatibility.md)。

### 已有资源

- 21 个课程讲稿 PDF（课程内部材料，发布在 Canvas，不入仓库）
- 课程大纲与教务材料（`reference/`，**不公开**，`.gitignore` 隔离）
- 5 个交互可视化 HTML（`code/visualizations/`，迁移自课程 Demo）
- AI 时代 21 讲课程蓝图、机器资源映射与旧卡覆盖迁移矩阵（`docs/curriculum/`，待课程组审批）
- 46 张卡片（`docs/cards/`，含 21 张来源锚点/概览卡和 25 张语义概念卡，已完成 AI 全量审核，统一为 `ai-reviewed`）
- 3 个深度专题（`docs/deep/`：LLM / 强化学习 / 量子计算）
- 2 个前沿注记页（`docs/frontier/`：LLM / CV，双层机制）
- 多路径索引（`docs/paths/` 五页）与 `glossary.md`
- 18 个概念示例、8 个核心实验、30 张 SVG 配图与跨平台 runner
- PAI-DSW Quickstart Notebook（持久化环境、example/Lab/可视化 helper 与学生工作备份）
- OpenCode 完整配置与 Pi 只读适配（共用 `course-tutor` / 5 skills / 10 个学习命令）
- `README.md` 与 `LICENSE`（内容 CC-BY-SA 4.0 / 代码 MIT）
- 2026 秋季课程网站源码与 GitHub Pages 自动部署（`website/`、`.github/workflows/pages.yml`）

### 待完成

- 3 次作业 30% / 项目 20% / 期末 40% / 课堂参与 10% 已确认；教师补齐题型细目并审批 `docs/assessment/blueprint.yaml` 后再启用“按正式考核结构校准”的 `/mock`
- 课程组审批 21 讲蓝图与 `lecture-card-map.yaml`
- 任课教师按 `docs/review/ai-audit-2026-08-22.md` 抽查 `ai-reviewed` 卡片；高风险内容再交相应领域专家
- 二期可选：英文版；更多深度专题
