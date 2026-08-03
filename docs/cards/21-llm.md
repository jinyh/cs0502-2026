---
title: 大语言模型
lecture: Slide21-LLM-2025
aliases: [LLM, 大语言模型, Transformer, 自监督预训练, 对齐, Agent, 涌现]
thinking_pillar: 智能思维
category: ai-ml
tags: [LLM, Transformer, 预训练, 对齐, RLHF, Agent, 涌现, 入门]
status: stable
version: 1.0
importance: 5
related_cards: [16-artificial-intelligence, 17-machine-learning, 03-programming-language]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-03
---

# 大语言模型（Large Language Model, LLM）

> 对应讲稿：[`Slide21-LLM-2025.pdf`](../../LectureNotes/Slide21-LLM-2025.pdf)

## 一句话定位

大语言模型（LLM）用海量文本自监督预训练 + 对齐微调，得到一个能理解指令、生成文本、调用工具的通用语言引擎。它是当前 AI 浪潮的核心，也催生了「Agent」范式。

## 核心知识点

### Token：LLM 的基本单位

文本被切成 token（子词单元），如「计算机」可能切为若干 token。LLM 的「词汇」是 token 而非字符或词。
- 直觉：token 介于字符和词之间，平衡词汇量与泛化。

### Transformer 架构（2017）

Vaswani 等提出，核心是**自注意力（self-attention）**：
- 每个 token 与序列中所有 token 计算注意力权重，决定「看哪儿」。
- 打破了 RNN 的顺序依赖，可大规模并行训练。
-decoder-only（如 GPT 系列）成为主流生成架构。

### 两阶段训练范式

1. **预训练（pre-training）**：在海量无标注文本上做**下一个 token 预测**（自监督）。学得语言规律与世界知识。
   - 目标：$\max_\theta \prod_t P(w_t \mid w_{<t})$
2. **对齐（alignment）/ 微调**：让模型「听指令、有用、无害」。
   - SFT（监督微调）：人工写指令-回答对。
   - RLHF / DPO：用人类偏好奖励优化。详见 `deep/llm-deep-dive.md`。

### 涌现能力（emergent abilities）

随规模（参数 / 数据 / 算力）增长，LLM 出现训练时未显式训练的能力（如少样本学习、链式推理）。这是「量变到质变」的观察，但学界对其是否真「涌现」有争议（可能是评估指标的非线性）。

### 幻觉（hallucination）

LLM 会生成看似合理但事实错误的内容。根因：它是统计生成而非检索——基于概率续写，不保证事实。缓解：RAG（检索增强生成）、工具调用、对齐、自校验。

### Agent：LLM 的新范式

把 LLM 作「大脑」，配以：
- **工具调用**（function calling）：搜索、代码执行、数据库查询。
- **记忆**（memory）：短期对话 + 长期向量检索。
- **规划**（planning）：把任务分解为多步。
形成能自主完成复杂任务的智能体。这正是本课程配套 OpenCode 智能体的技术基础。

### LLM 与编程语言（关联 03）

LLM 与传统编程语言对照（见 `03-programming-language`）：
- 传统语言：精确、确定、人类写规则。
- LLM：模糊、概率性、从数据归纳「规则」。
- 趋势：自然语言正成为新的「编程接口」——用自然语言指挥 LLM/Agent。

## 直觉类比（跨学科桥接）

| 概念 | 类比 |
|---|---|
| 预训练 | 读了全人类图书馆的人，什么都懂一点 |
| 对齐微调 | 教这个博学者「怎么跟人合作、什么不该说」 |
| 自注意力 | 阅读时根据上下文决定哪些词更重要（「苹果」在水果公司里重哪边） |
| 幻觉 | 博学者有时记混、自信地编造——听起来对但查无实据 |
| Agent | 给博学者配电脑、电话、笔记本，能主动办事 |
| Token | 介于「字」和「词」之间的最小语义单元 |

## 前沿进展注记

LLM 前沿变化最快，本卡片只给框架。**最新进展必须查 [`frontier/llm-frontier.md`](../frontier/llm-frontier.md) 与 [`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)**，而非依赖卡片静态内容。

智能体应联网补充（见 `opencode/AGENTS.md`），约定见 `frontier/` 机制。开放问题：长程推理、对齐税、训练数据枯竭、可解释性、Agent 可靠性。

## 跨学科联系

- **与语言学**：LLM 挑战了乔姆斯基「先天语法」观——统计学习似乎也能掌握语言，但语义与语用仍有距离。
- **与认知科学**：注意力机制 vs 人脑注意；预测编码理论。
- **与医学**：医学问答、病历摘要、文献综述；但医疗幻觉风险高，需 RAG + 人工复核。
- 与材料/生物医药：药物发现的文献挖掘与分子性质预测借助 LLM；材料信息学的非结构化报告抽取。


## 推荐交互式问答

1. 预训练和对齐分别解决什么问题？为什么只预训练不够？
2. Transformer 的自注意力解决了 RNN 的什么痛点？
3. 幻觉为什么是 LLM 的「特性」而非「bug」？能根除吗？
4. LLM Agent 比单纯 LLM 强在哪？它依赖什么外部能力？（工具/记忆/规划）
5. 用自然语言指挥 LLM 写代码，和直接写 Python，本质区别是什么？（关联 `03`）

## 代码示例

```python
# 对应 docs/cards/21；最简 tokenizer 直觉：字符级 BPE 思路
# 运行：uv run python code/examples/21_mini_tokenizer.py
from collections import Counter

def char_ngrams(text, n=3):
    """把文本切成 n-gram，模拟 tokenization 的最简形式"""
    return [text[i:i+n] for i in range(0, len(text)-n+1)]

def next_token_demo(model, context, vocab):
    """下一个 token 预测的玩具版：基于统计计数"""
    c = Counter()
    for w1, w2, w3 in zip(model, model[1:], model[2:]):
        if (w1, w2) == context: c[w3] += 1
    total = sum(c.values())
    return {t: cnt/total for t, cnt in c.items()} if total else {}

text = "计算机科学导论课程计算机科学很有趣计算机科学导论很重要"
ngrams = char_ngrams(text)
print("token 序列:", ngrams[:8])
prob = next_token_demo(ngrams, ('计算机', '算机科'), ngrams)
print("下一 token 概率:", prob)  # 统计频次，真实 LLM 用神经网络
```

## 延伸阅读

- 对应讲稿 `Slide21-LLM-2025.pdf`。
- 关联：`16`（AI 范式）、`17`（ML 基础）、`03`（编程语言对照）。
- 深度专题：[`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)（架构/训练/对齐/Agent/前沿全景）。
- 原始文献：Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS*.
