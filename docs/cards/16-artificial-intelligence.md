---
title: 人工智能
lecture: Slide16-ArtificialIntelligence-2025
aliases: [AI, 人工智能, 符号主义, 连接主义, 图灵测试, 智能体]
thinking_pillar: 智能思维
category: ai-ml
tags: [人工智能, 图灵测试, 符号主义, 连接主义, 智能体, 入门]
status: stable
version: 1.0
importance: 5
related_cards: [02-intro-to-cs, 17-machine-learning, 21-llm]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-03
---

# 人工智能（Artificial Intelligence）

> 对应讲稿：[`Slide16-ArtificialIntelligence-2025.pdf`](../../LectureNotes/Slide16-ArtificialIntelligence-2025.pdf)

## 一句话定位

人工智能（Artificial Intelligence, AI）研究如何让机器表现出「智能」行为。它的边界与定义一直在移动——曾经被视为 AI 的下棋程序，今天已不算智能。**AI 不是单一技术，而是一个研究纲领**。

## 核心知识点

### 图灵测试（Turing Test）

Turing（1950）提出：若机器在自由对话中让人无法分辨它是人是机器，则可称智能。它把「智能」操作化为「行为不可分辨」，避开了定义「意识」的哲学泥潭。今天 LLM 已能在对话上通过弱化版图灵测试，但这不等于真正理解——引发新讨论。

### 三大范式

- **符号主义（symbolicism）**：智能 = 符号操作 + 规则推理。代表：专家系统、逻辑编程。1980s 达峰后因「知识获取瓶颈」衰落。
- **连接主义（connectionism）**：智能 = 神经网络学习。代表：深度学习。2012 年 AlexNet 后主导 AI。
- **行为主义（actionism）**：智能 = 感知-动作的适应性。代表：强化学习、机器人控制。

三者非互斥，现代 AI（尤其 Agent）常融合三者。

### 弱 AI vs 强 AI

- **弱 AI（narrow AI / weak AI）**：在特定任务上达到人类水平或更强（如下棋、识别、翻译）。当前所有实用 AI 都属此类。
- **强 AI（AGI / strong AI）**：具备通用认知能力，跨域迁移。**尚未实现**，是否可能仍是开放问题。

### 智能体（Agent）

AI 的一个核心抽象：**智能体（agent）**感知环境、决策、行动、影响环境。
- 形式：$Agent: Percept \to Action$。
- 类型：简单反射 agent、基于模型的反射 agent、目标驱动、效用驱动、学习型 agent。
- LLM 时代的 Agent：以大模型为「大脑」+ 工具调用 + 记忆，自主完成多步任务（见 `21-llm`）。

### AI 的能力边界

- 擅长：模式识别、统计预测、大规模数据处理。
- 不擅长：因果推理、常识、可解释决策、样本效率。
- 不可解：停机问题等理论限制同样适用于 AI（见 `08-turing-machine`）。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| 符号主义 | 遵循诊疗指南逐步推理的医生（规则驱动） |
| 连接主义 | 通过看千万张影像积累直觉的放射科医生（经验驱动） |
| 强化学习 agent | 试错学会走迷宫的实验动物 |
| 图灵测试 | 「以貌取人」不可靠，于是只听声音判断——行为不可分辨 |
| 弱 vs 强 AI | 计算器算得快但不「懂数学」；当前 AI 多是「会考试」而非「懂世界」 |

## 前沿进展注记

AI 前沿变化极快，本卡片只给框架。具体进展见 [`frontier/`](../frontier/) 与 [`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)：
- 当前主线：大模型 + Agent 工具调用 + 多模态融合。
- 开放问题：幻觉、对齐（alignment）、可解释性、样本效率、通用智能边界。

智能体可联网补充最新进展（见 `opencode/AGENTS.md` 前沿检索约定）。

## 跨学科联系

- **与哲学**：图灵测试与「意识」「心智」的关系；中文房间论证（Searle）质疑「理解」。
- **与神经科学**：神经网络最初受生物神经元启发，但今天的深度网络是高度抽象，非脑仿真。
- **与医学**：医学影像 AI、电子病历分析、药物发现；同时引发医疗责任与偏见问题（见 `computing-ethics` 可选扩展）。
- **与经济学**：AI 作为一个经济 agent 参与博弈；就业结构变化。

## 推荐交互式问答

1. 符号主义和连接主义对「智能是什么」的回答分别是什么？各举一个失效场景。
2. 图灵测试通过就能说机器「理解」吗？中文房间论证怎么反驳？
3. 弱 AI 和强 AI 的区别为什么重要？当前 LLM 属于哪一类？
4. 一个医疗影像 AI 把「没病」判成「有病」可能比相反严重得多——这反映了 AI 决策的什么特征？

## 代码示例

```python
# 对应 docs/cards/16；一个最简反射 agent：扫地机器人
# 运行：uv run python code/examples/16_reflex_agent.py

class ReflexVacuumAgent:
    """简单反射 agent：基于条件-动作规则，无记忆"""
    def __init__(self):
        self.rules = {
            ('脏', 'A'): '吸',
            ('脏', 'B'): '吸',
            ('干净', 'A'): '右',
            ('干净', 'B'): '左',
        }
    def act(self, location, status):
        return self.rules.get((status, location), '停')

if __name__ == "__main__":
    agent = ReflexVacuumAgent()
    print(agent.act('A', '脏'))   # 吸
    print(agent.act('A', '干净')) # 右
    print(agent.act('B', '脏'))   # 吸
```

## 延伸阅读

- 对应讲稿 `Slide16-ArtificialIntelligence-2025.pdf`。
- 关联：`17`（机器学习——连接主义的实现）、`21`（LLM 与 Agent）。
- 深度专题：[`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)。
- 经典教材：Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*, 4th ed.
