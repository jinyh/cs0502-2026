---
title: 语音识别
lecture: Slide20-SpeechRecognition-2025
aliases: [语音识别, ASR, 声学模型, 语言模型, 序列建模]
thinking_pillar: 智能思维
category: ai-ml
tags: [语音识别, ASR, 声学, 语言模型, 序列建模, 入门]
status: stable
version: 1.0
importance: 3
related_cards: [17-machine-learning, 21-llm, 18-computer-vision]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-03
---

# 语音识别（Speech Recognition）

> 对应讲稿：[`Slide20-SpeechRecognition-2025.pdf`](../../LectureNotes/Slide20-SpeechRecognition-2025.pdf)

## 一句话定位

语音识别（Automatic Speech Recognition, ASR）把声学信号映射为文字。它是序列到序列建模的经典案例，也是多模态大模型的重要模态之一。

## 核心知识点

### 语音的信号本质

- 声音是一维时序波形（采样率如 16kHz）。
- 预处理：分帧 → 加窗 → 提取声学特征（如 MFCC、Mel 频谱）。
- 直觉：把连续声波切成短窗，每窗算「这一刻的声音颜色」。

### ASR 的三段式经典流程

1. **声学模型（acoustic model）**：声学特征 → 音素概率。
2. **语言模型（language model）**：约束「什么字组合更可能」。
3. **解码（decoding）**：结合两者搜索最可能文字序列（如 Viterbi、CTC）。

### 技术演进

- HMM-GMM：经典统计模型时代。
- 深度学习：DNN/RNN/LSTM 替代声学模型。
- 端到端：CTC、Attention/Seq2Seq、Transformer 直接从音频到文字。
- Conformer / 大规模预训练 ASR（Whisper 等）。

### 评价指标

- 词错率（Word Error Rate, WER）：编辑距离 / 参考词数。
- 注意：WER 低不等于可用，需结合场景（噪声/口音/专业词）。

### 挑战

- 远场与噪声、口音与方言、专业词汇、低资源语言。
- 实时性 vs 准确率权衡。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 声学特征 | 把声音切成「颜色块」 |
| 语言模型 | 听不清时用上下文猜——「下雨天留人*客*」还是「*天*」 |
| 解码 | 在所有可能字串里找综合最像的 |
| 端到端 | 不分阶段，直接从声波到文字 |

## 前沿进展注记

- Whisper 等大规模多语言 ASR 把识别拉到接近人类水平（多数场景）。
- 多模态：音频 + 视觉（唇读）+ 文本联合建模。
- 语音合成（TTS）与 ASR 对称发展，支持实时同传。
- 本课程配套的 OpenCode 智能体未来可加语音输入模态。

## 跨学科联系

- 与语言学：音素、韵律、语用；ASR 把语音学形式化。
- 与信号处理：傅里叶变换、滤波是基础工具。
- 与医学：助听器、ALS 患者语音辅助、喉部术后语音康复。
- 与认知：人脑的语音感知也是声学+语言上下文双路。

## 推荐交互式问答

1. ASR 为什么需要语言模型？光有声学模型不够吗？
2. 端到端模型相比三段式有什么优劣？
3. 医学口述病历 ASR 的特殊挑战是什么？（专业词/隐私）
4. 语音识别和文本生成（LLM）在「序列建模」上有什么共性？

## 延伸阅读

- 对应讲稿 `Slide20-SpeechRecognition-2025.pdf`。
- 关联：`17`（ML 方法）、`21`（语言模型与大模型）。
- 经典：Huang, X. et al. (2014). *Spoken Language Processing*.
