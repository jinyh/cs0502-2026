---
title: 多模态感知：图像、语音与跨模态表示
card_id: multimodal-models
lecture_refs: [L19, L20, L21]
source_slides: [Slide18-ComputerVision-2025, Slide20-SpeechRecognition-2025, Slide21-LLM-2025]
aliases: [多模态, 计算机视觉, 语音识别, 表示对齐, 模态融合]
thinking_pillars: [数据思维, 智能思维]
category: ai-ml
tags: [图像, 语音, 文本, 多模态, 编码器, 融合, 对齐, 评价]
status: ai-reviewed
version: 1.0
importance: 4
learning_objectives: [比较不同模态的采样与误差, 解释编码对齐和融合流程, 为多模态任务设计分层评价]
prerequisites: [data-representation, neural-networks-transformers]
estimated_minutes: 40
assessment_tags: [模态比较, 系统追踪, 误差分析, 评价设计]
labs: []
figures: [18-convolution.svg, 20-rnn-asr.svg]
related_cards: [data-representation, neural-networks-transformers, 18-computer-vision, 20-speech-recognition, 19-recommend-system, ml-evaluation]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-22
---

# 多模态感知：图像、语音与跨模态表示（Multimodal Learning）

> 新课程位置：L19。CV、语音和推荐不再各占一讲，而作为共享表示与评价原理下的案例卡继续保留。

## 一句话定位

多模态系统把图像、语音、文本等不同采样过程映射到可比较或可联合推理的表示；融合信息的同时，也会继承每种传感、标注和评价的误差。

## 学完应能做到

1. 比较图像、语音和文本从物理/符号世界到张量表示的采样与误差来源。
2. 解释模态编码、表示对齐、融合和任务输出的基本链路。
3. 为多模态任务分别评价单模态质量、跨模态一致性、最终任务和群体风险。

## 核心知识点

### 每种模态先有自己的表示问题

- 图像由空间采样、颜色通道和位深构成，受光照、视角、设备和压缩影响。
- 语音由时间采样和频谱表示构成，受噪声、口音、语速、麦克风和分段影响。
- 文本依赖语言、分词和上下文，可能丢失语气、视觉布局与隐含背景。
- 传感阶段丢失的信息不能因为把数据送进“大模型”而恢复。

### 编码、对齐与融合

- 每个模态编码器把原始输入变成向量或序列表示。
- 对齐使相关图像—文本、语音—文本或视频—动作在表示空间建立联系。
- 早期融合在输入/低层特征组合，晚期融合组合各模型决策；中间交互允许更细关联。
- 缺失模态、时间不同步和相互矛盾是实际系统必须处理的状态。

### 应用共享原理但错误不同

- CV 的分类、检测和分割有不同输出粒度与标注成本。
- ASR 的词错误率把替换、删除和插入合并，但不直接表示语义伤害。
- 推荐系统融合文本、图像、行为和图结构时，还受反馈循环与曝光偏差影响。
- 多模态生成可能产生文本与图像互相不一致的幻觉。

### 分层评价

- 输入层：清晰度、噪声、缺失、设备和覆盖。
- 表示层：检索、对齐或嵌入是否保留任务相关信息。
- 任务层：分类、检测、转写、问答或生成指标。
- 系统层：时延、资源、可解释性、群体差异、安全与人工工作流。

## 工程桥接

- 医学影像与报告联合模型需要处理报告时间、设备差异和“文本是否泄漏诊断标签”。
- 工业巡检可组合图像、声音和传感器曲线，但传感器不同步会造成假关联。
- 无障碍字幕系统除了 WER，还要评价专业词、说话人和延迟对真实交流的影响。

## 常见误区与边界

- “多模态一定优于单模态”错误：额外模态可能噪声更大、缺失或引入泄漏。
- “共享嵌入空间意味着模型理解同一概念”过度推断。
- “总体指标提高”可能掩盖某口音、设备或影像类型退化。
- 模态更多也扩大隐私与攻击面，应遵循数据最小化。

## 主动学习与考核迁移

- **比较**：为同一事件列出相机、麦克风和文字记录分别可能丢失的信息。
- **故障链**：音画不同步会怎样影响训练对齐和最终结论？
- **评价**：为医学影像问答设计输入、对齐、任务和系统四层指标。
- **迁移**：当语音缺失时，多模态设备诊断系统应拒绝、降级还是继续？写出条件。

## 与课程图谱关系

- 编码与量化见 [`data-representation`](data-representation.md)。
- 模型结构见 [`neural-networks-transformers`](neural-networks-transformers.md)。
- 单模态案例见 [`18-computer-vision`](18-computer-vision.md) 和 [`20-speech-recognition`](20-speech-recognition.md)。
- 评价见 [`ml-evaluation`](ml-evaluation.md)。

## 延伸阅读

- Baltrušaitis, T., Ahuja, C. & Morency, L.-P. (2019). Multimodal Machine Learning: A Survey and Taxonomy. *IEEE TPAMI*.
- Jurafsky, D. & Martin, J. *Speech and Language Processing*.
