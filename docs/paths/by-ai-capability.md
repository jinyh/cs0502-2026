# 学习路径：按 AI 能力形成

> 按 AI 从感知到行动的能力链条组织，适合关注「AI 能做什么、怎么做的」的读者。

## 感知（Perception）

让机器接收并理解外部世界信号。

- [`18-computer-vision`](../cards/18-computer-vision.md) — 视觉感知
- [`20-speech-recognition`](../cards/20-speech-recognition.md) — 听觉感知
- [`multimodal-models`](../cards/multimodal-models.md) — 图像、语音、文本的表示、对齐与融合
- 前沿：[`cv-frontier`](../frontier/cv-frontier.md)

## 学习（Learning）

从数据中归纳规律。

- [`17-machine-learning`](../cards/17-machine-learning.md) — 学习三范式
- [`14-data-mining`](../cards/14-data-mining.md) — 大规模数据的知识发现
- [`ml-evaluation`](../cards/ml-evaluation.md) — 泛化、泄漏、指标、偏差与漂移
- 深度：[`reinforcement-learning`](../deep/reinforcement-learning.md) — 从反馈学习

## 推理（Reasoning）

基于知识与规则推断。

- [`computability-limits`](../cards/computability-limits.md) — 可计算性与自动化边界
- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) — AI 历史范式
- [`ai-search-planning-agents`](../cards/ai-search-planning-agents.md) — 状态空间、知识表示与规划

## 生成（Generation）

创造新内容。

- [`21-llm`](../cards/21-llm.md) — 语言生成
- [`neural-networks-transformers`](../cards/neural-networks-transformers.md) — 注意力与 Transformer 共享结构
- [`rag-tool-agents`](../cards/rag-tool-agents.md) — 用检索和引用约束生成

## Agent（行动）

感知→决策→行动的闭环。

- [`16-artificial-intelligence`](../cards/16-artificial-intelligence.md) — 智能体抽象
- [`ai-search-planning-agents`](../cards/ai-search-planning-agents.md) — 观察—决策—行动闭环
- [`rag-tool-agents`](../cards/rag-tool-agents.md) — LLM、RAG 与工具编排
- [`ai-security`](../cards/ai-security.md) — 权限、注入与不可信输出
- [`responsible-ai-systems`](../cards/responsible-ai-systems.md) — 证据、治理、监测与问责
- 深度：[`llm-deep-dive`](../deep/llm-deep-dive.md) 第 5 节（Agent 与工具调用）
- 本课程配套的 OpenCode 智能体（[`opencode/knowledge.md`](../../opencode/knowledge.md)）即此路径的实例

> 链条非线性：Agent 需要前四者全部。本路径推荐先建立「学习」基座，再按「感知→生成→Agent」展开。
