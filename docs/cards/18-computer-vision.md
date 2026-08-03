---
title: 计算机视觉
lecture: Slide18-ComputerVision-2025
aliases: [计算机视觉, CV, 图像分类, 检测, CNN, 分割]
thinking_pillar: 智能思维
category: ai-ml
tags: [计算机视觉, CNN, 图像分类, 目标检测, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [17-machine-learning, 16-artificial-intelligence]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-03
---

# 计算机视觉（Computer Vision）

> 对应讲稿：[`Slide18-ComputerVision-2025.pdf`](../../LectureNotes/Slide18-ComputerVision-2025.pdf)

## 一句话定位

计算机视觉（Computer Vision, CV）让机器从图像/视频中提取语义——「看见」并「看懂」。它是深度学习最先取得突破的领域（2012 AlexNet），也是医学影像 AI 的核心技术。

## 核心知识点

### 图像的数字表示

- 图像 = 像素（pixel）阵列；灰度图是 2D 矩阵，彩图是 $H\times W\times 3$（RGB 三通道）。
- 像素值 0–255（8 bit）。机器「看」到的是数字，不是画面。

### 经典任务

- **分类（classification）**：整图打一个标签。
- **检测（detection）**：定位 + 分类多个目标（边界框）。
- **分割（segmentation）**：逐像素分类（语义/实例分割）。
- **生成（generation）**：从文本/草图生成图像。

### CNN（Convolutional Neural Network）

卷积神经网络利用图像的**局部性**与**平移不变性**：
- 卷积层：小核滑窗提取局部特征（边缘→纹理→部件→对象，层次化）。
- 池化层：降采样，增加感受野与不变性。
- 深层网络学得从低级到高级的层次特征——这是深度学习优于手工特征的关键。

### 里程碑

- AlexNet (2012)：深度学习在 ImageNet 碾压传统方法，开启深度学习时代。
- ResNet (2015)：残差连接使超深网络可训练。
- Vision Transformer (ViT, 2020)：把 Transformer 引入视觉，挑战 CNN 主导。

### 数据与评估

- ImageNet 等大规模标注数据集是关键。
- 评估：准确率、mAP、IoU。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 像素阵列 | 马赛克瓷砖的颜色编号 |
| 卷积核 | 用小放大镜扫描，找特定纹理 |
| CNN 层次 | 从笔画→偏旁→字→句的层次识别 |
| 检测 | 不只说「有猫」，还圈出在哪 |

## 前沿进展注记

CV 前沿变化快：
- 多模态大模型（如 CLIP、GPT-4V）统一视觉与语言。
- 扩散模型（Diffusion）主导图像生成。
- 自监督预训练减少标注依赖。
具体见 [`frontier/cv-frontier.md`](../frontier/cv-frontier.md) 与 [`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)（多模态部分）。

## 跨学科联系

- 与神经科学：CNN 受视觉皮层感受野启发（Hubel & Wiesel）。
- 与医学：CT/MRI/病理 AI 辅助诊断——但分布偏移（设备/人群差异）是落地难题。
- 与物理：成像原理（光学/CT 重建）决定输入数据特性。
- 与航空航天/地球科学：遥感影像处理（目标识别、变化检测、地学大数据）是 CV 的大规模应用；无人机视觉导航。

## 推荐交互式问答

1. 机器「看」到的图像是什么？和人看到的「画面」有何不同？
2. CNN 的卷积核为什么比全连接层更适合图像？
3. 医学影像 AI 在三甲训练，到基层部署可能出什么问题？
4. 多模态大模型（GPT-4V）和专门 CNN 各有什么优劣？

## 延伸阅读

- 对应讲稿 `Slide18-ComputerVision-2025.pdf`。
- 关联：`17`（ML 基础）、`16`（AI 范式）。
- 经典：Goodfellow, I. et al. (2016). *Deep Learning*, Ch.9.
