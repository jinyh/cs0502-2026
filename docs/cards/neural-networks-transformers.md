---
title: 神经网络、注意力与 Transformer
card_id: neural-networks-transformers
lecture_refs: [L19, L20]
source_slides: [Slide17-MachineLearning-2025, Slide18-ComputerVision-2025, Slide20-SpeechRecognition-2025, Slide21-LLM-2025]
aliases: [神经网络, 反向传播, CNN, RNN, 注意力, Transformer]
thinking_pillars: [智能思维, 系统思维]
category: ai-ml
tags: [神经元, 层, 激活, 损失, 梯度, CNN, RNN, attention, Transformer]
status: ai-reviewed
version: 1.0
importance: 5
learning_objectives: [追踪小型网络前向计算, 比较CNN RNN Transformer结构偏置, 分析训练推理和资源代价]
prerequisites: [17-machine-learning, data-representation, probability-uncertainty]
estimated_minutes: 55
assessment_tags: [模型追踪, 架构比较, 结构选择, 资源分析]
labs: [lab-07-machine-learning, lab-08-language-model]
figures: [17-neural-learning.svg, 18-convolution.svg, 20-rnn-asr.svg, 21-language-model-evolution.svg]
related_cards: [17-machine-learning, 18-computer-vision, 20-speech-recognition, 21-llm, computer-architecture, multimodal-models]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-22
---

# 神经网络、注意力与 Transformer（Neural Networks and Transformers）

> 新课程位置：L19；把旧 `17/18/20/21` 中重复出现的模型结构抽成共享原理卡。

## 一句话定位

神经网络通过可学习参数组合表示；CNN、RNN 和 Transformer 的关键差别在于它们如何利用局部、顺序与全局关系，以及为此付出什么数据和计算代价。

## 学完应能做到

1. 手算一个小型神经元、卷积或注意力例子的前向输出。
2. 比较 CNN、RNN 和 Transformer 对局部性、顺序、并行性和长距离依赖的处理。
3. 综合数据规模、延迟、内存、能耗和错误代价选择模型家族。

## 核心知识点

### 从线性组合到多层表示

- 神经元计算加权和 $z=w^Tx+b$，再经激活函数产生输出。
- 多层网络把简单变换组合成复杂函数；宽度和深度提高表示能力，也增加训练难度和过拟合风险。
- 损失函数把预测与目标差异变成优化信号；梯度下降沿局部下降方向更新参数。
- 反向传播利用链式法则高效计算梯度，不等于模型“理解了错误原因”。

### CNN：局部与平移结构

- 卷积核在不同位置共享参数，适合局部模式重复出现的网格数据。
- 层叠卷积扩大感受野，从边缘等局部特征组合到更高层表示。
- CNN 不是只用于图像；任何具有局部邻域结构的数据都可能使用。

### RNN：递归状态与顺序

- RNN 用隐藏状态汇总之前的信息，天然按序列步骤处理。
- 长序列训练可能遇到梯度消失/爆炸；门控结构缓解但不消除所有困难。
- 串行依赖限制并行训练，也使很远信息难以直接交互。

### 注意力与 Transformer

- 注意力用 query 与 key 的匹配决定对各 value 的加权汇总。
- 自注意力让序列位置直接交互；位置编码提供顺序信息。
- Transformer 便于并行训练并建模长距离关系，但标准全注意力的计算和内存随序列长度快速增长。
- 多头、层归一化、残差等组件服务稳定训练；导论重点是信息流和结构偏置。

## 工程桥接

- 医学影像分类可能利用 CNN 或视觉 Transformer，但跨设备泛化比单一测试分数更关键。
- 设备声音监测既有局部频谱模式，也有时间依赖，可组合卷积和注意力。
- 边缘部署需考虑低精度、剪枝、内存和热设计，不只比较参数量。

## 常见误区与边界

- “深度网络会自动学习所有特征”错误：数据、目标、架构和训练过程共同塑造捷径。
- “Attention is all you need”是特定论文标题，不表示系统不需要数据、优化、存储或安全。
- “参数更多必然更好”忽略数据质量、评价、推理成本和任务规模。
- 架构图能解释信息流，不能证明内部表示等同于人类概念。

## 最小代码观察

- 用 [`17_generalization.py`](../../code/examples/17_generalization.py) 观察复杂度与泛化。
- 用 [`21_ngram.py`](../../code/examples/21_ngram.py) 对比统计语言模型，为注意力模型的上下文处理建立基线。
- 手算 [`18-convolution.svg`](../../figures/18-convolution.svg) 中的小卷积，不先运行库函数。

## 主动学习与考核迁移

- **手算**：给两个二维向量，计算缩放前的点积注意力分数并做归一化解释。
- **比较**：图像边缘、语音帧序列和长文档分别需要哪种结构偏置？
- **资源**：上下文长度翻倍时，标准全注意力的交互对数如何变化？这不等于哪些实际运行结论？
- **迁移**：为边缘故障检测选择小 CNN、RNN 或 Transformer，并列出待实测的准确率、时延、内存和能耗。

## 与课程图谱关系

- 学习与泛化基础见 [`17-machine-learning`](17-machine-learning.md) 和 [`ml-evaluation`](ml-evaluation.md)。
- 硬件代价见 [`computer-architecture`](computer-architecture.md)。
- 多模态应用见 [`multimodal-models`](multimodal-models.md)。
- 语言生成见 [`21-llm`](21-llm.md)。

## 延伸阅读

- Goodfellow, I., Bengio, Y. & Courville, A. *Deep Learning*.
- Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS*.
