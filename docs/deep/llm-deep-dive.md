---
title: LLM 深度专题
aliases: [大语言模型, Transformer, 预训练, 对齐, RLHF, Agent, 多模态]
category: ai-ml
tags: [LLM, Transformer, 预训练, SFT, RLHF, DPO, Agent, 多模态, 涌现]
status: ai-reviewed
version: 1.1
importance: 5
authoritative_cards: [21-llm, 16-artificial-intelligence, 17-machine-learning]
last_reviewed: 2026-08-22
---

# 大语言模型深度专题（LLM Deep Dive）

> 对应卡片：[`21-llm`](../cards/21-llm.md)、[`16-artificial-intelligence`](../cards/16-artificial-intelligence.md)、[`17-machine-learning`](../cards/17-machine-learning.md)
> 前沿增量：[`llm-frontier.md`](../frontier/llm-frontier.md)（本页静态层与前沿页互补）

本专题在卡片框架上展开 LLM 的架构、训练、对齐、应用与前沿，供需要深入理解的学生使用。非 CS 背景学生可只读「直觉先行」小节。

## 1. 历史脉络

- 2017：Vaswani 等提出 Transformer，自注意力打破 RNN 顺序依赖。
- 2018：BERT（encoder-only，理解）、GPT-1（decoder-only，生成）确立预训练范式。
- 2020：GPT-3（175B）展示少样本学习与规模涌现。
- 2022：ChatGPT（RLHF 对齐）引爆公众认知。
- 2023+：开放权重模型、多模态模型、工具型 Agent 与增加推理时计算的方法持续发展；具体产品能力应在前沿页按日期核验。

## 2. 架构原理

### 2.1 自注意力（Self-Attention）

序列中每个位置对所有位置计算相关性，加权聚合。直觉：阅读时，每词根据上下文决定「重点看哪些词」。

缩放点积注意力：

$$\text{Attention}(Q,K,V)=\text{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

其中 $Q,K,V$ 是输入经三个线性变换得到的查询、键、值矩阵；$\sqrt{d_k}$ 防止点积过大导致 softmax 饱和。

### 2.2 多头注意力（Multi-Head）

并行多组 $Q/K/V$，每组在不同子空间学不同关系（如语法 vs 语义），拼接后投影。类比：多角度同时观察。

### 2.3 decoder-only 结构

现代生成 LLM（GPT 系）用 decoder-only：自回归预测下一个 token。每层 = 多头注意力 + 前馈网络 + 残差 + 层归一化。位置编码（RoPE 等）注入位置信息。

### 2.4 规模化要素

性能与参数量、数据量和算力的共同配置相关。Chinchilla 工作在特定实验假设下给出计算最优缩放关系；“约 20 token/参数”是该研究设置中的经验结果，不是所有模型、数据质量和训练目标的固定定律。

## 3. 训练范式

### 3.1 预训练（Pre-training）

- 目标：下一个 token 预测（自监督，无需标注）。
- 损失：交叉熵 $\mathcal{L}=-\sum_t \log P(w_t\mid w_{<t})$。
- 数据：海量网页/书籍/代码，去重去毒。
- 结果：一个「什么都能续写」的基座模型，但不会「听指令」。

### 3.2 对齐（Alignment）三阶段

1. **SFT（Supervised Fine-Tuning）**：用人工写的「指令-回答」对微调，让模型学会「按指令作答」。
2. **奖励建模（Reward Model）**：训练一个能给回答打分的模型，输入人类偏好对比。
3. **RLHF / DPO**：
   - RLHF：用奖励模型作奖励信号，PPO 强化学习优化 SFT 模型。
   - DPO：直接用偏好对优化，绕过显式奖励模型，更简单稳定。

对齐解决「有用、诚实、无害」三目标间的张力——三者常冲突，无完美解。

### 3.3 高效适配

- LoRA：只训练注入的低秩矩阵，参数高效微调。
- RAG：不更新模型参数，而把检索到的外部材料加入上下文；在检索、引用和评测设计得当时可改善可溯源性。在医疗、法律等高风险场景中它只是候选组件，仍需数据治理、专业验证、权限控制与责任流程。
- 模型量化：4-bit/8-bit 推理降低部署门槛。

## 4. 能力与局限

### 4.1 涌现能力

随规模增长出现少样本学习、思维链推理等。但学界对「真涌现 vs 评估指标非线性」有争议——部分能力可能在更细粒度指标下是平滑增长的。

### 4.2 幻觉

幻觉与训练目标、数据、知识覆盖、上下文依据、解码和系统编排共同相关，不能归结为单一根因。RAG、工具调用、降低采样随机性和外部核验可能缓解，但都不能保证根除。

### 4.3 上下文窗口与长程

上下文窗口从千级到百万级。但「能装」≠「能用好」——长上下文中存在「迷失中段」现象，模型对中间信息利用率低。

### 4.4 可解释性

LLM 内部机制尚不能被完整、可靠地解释。机械可解释性（mechanistic interpretability）尝试定位特征与计算“电路”，但当前解释覆盖、因果有效性和跨模型泛化仍有限。

## 5. 应用与 Agent 范式

### 5.1 从对话到 Agent

LLM 作「大脑」+ 工具调用 + 记忆 + 规划，构成能自主完成多步任务的 Agent。典型循环：感知 → 规划 → 行动（调工具）→ 观察 → 再规划。

### 5.2 工具调用（Function Calling）

模型输出结构化的工具调用请求（如查数据库、跑代码、检索），由外部执行器执行并把结果回灌上下文。这是 LLM 连接真实世界的接口。

### 5.3 多智能体协作

多个角色化 Agent 可用于辩论、分工或交叉检查；已有结果依赖任务与编排，有时改善表现，也可能放大错误、通信成本和责任不清，必须与单 Agent 基线比较。

### 5.4 推理模型

一类推理模型在回答前使用更多推理时计算，并在部分数学、编程等基准上改善结果。模型内部计算不等同于可靠、完整或可见的人类思维链，评价时仍应检查答案、证据、时延与成本。

## 6. 前沿与开放问题

> 静态层基线，最新进展见 [`llm-frontier.md`](../frontier/llm-frontier.md)。

- **对齐税**：对齐后能力下降，如何对齐不损能力。
- **训练数据与数据质量**：可授权、高质量且适配任务的数据供给是否成为瓶颈仍是开放问题；合成数据与自我改进可能补充，也可能累积偏差。
- **效率**：推理成本、长上下文、KV 缓存优化、MoE 稀疏激活。
- **多模态统一**：视觉/音频/动作统一到 token 序列。
- **安全**：滥用（生物/网络）、越狱、误导性输出。
- **基础科学**：scaling law 的理论解释、智能涌现机制、与大脑的关系。
- **评估困境**：基准污染、能力难量化、泛化到何处的边界不清。

## 7. 跨学科联系

- **语言学**：LLM 的「语言能力」挑战先天语法论；但语用与具身认知仍缺。
- **认知科学**：预测编码、注意力的神经对应。
- **材料/生物医药**：药物发现的文献挖掘、分子性质的自然语言描述抽取、合成路线规划辅助——但化学事实性幻觉风险高，须 RAG + 实验核实。

- **哲学**：「随机鹦鹉」之争、理解 vs 模拟、对齐的价值对齐难题。

## 8. 与本课程的关系

本仓库配套的 OpenCode 智能体（`opencode/`）即以 LLM 为引擎加载知识库。`AGENTS.md` 的教学红线（不代写、不碰敏感数据、直觉先行）正是「对齐」在课程场景的落地——技术上的对齐靠 SFT/RLHF，场景上的对齐靠 AGENTS.md 约束。

## 延伸阅读

- 综述：Zhao, W. et al. (2023). *A Survey of Large Language Models*. arXiv:2303.18223.
- 原始：Vaswani, A. et al. (2017). Attention Is All You Need. NeurIPS.
- 对齐：Ouyang, L. et al. (2022). Training language models to follow instructions. NeurIPS.
- DPO：Rafailov, R. et al. (2023). Direct Preference Optimization. NeurIPS.
- 推理：Wei, J. et al. (2022). Chain-of-Thought Prompting. NeurIPS.
- 工具：Schick, T. et al. (2023). Toolformer. NeurIPS.
