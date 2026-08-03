---
topic: Computer Vision
last_static_review: 2026-08-03
authoritative_card: 18-computer-vision.md
deep_dive: llm-deep-dive.md
status: living
---

# 计算机视觉前沿进展注记

> 本页采用双层机制，详见 [`frontier/README.md`](README.md)。

## 静态写底层（人工审校，季度更新）

### 2026 基线

- **架构多元**：CNN 与 Vision Transformer (ViT) 并存；ViT 在大规模数据上展现优势，CNN 因归纳偏置在中小数据仍占优。
- **多模态统一**：CLIP 类视觉-语言对比学习成为标配预训练；多模态大模型（GPT-4V 等）把视觉作为 token 模态接入 LLM。
- **图像生成**：扩散模型（Diffusion）主导高质量生成；条件生成（文本到图像、图像编辑）能力显著提升。
- **自监督**：MAE 等掩码自编码减少对标注依赖。
- **3D 视觉**：神经辐射场（NeRF）、3D 高斯泼溅推动可微渲染与新视角合成。
- **医学影像**：分割与分类在专科任务上接近专家，但分布偏移（设备/人群）仍是落地障碍。

### 关键开放问题

- 多模态大模型是否会让专门 CNN 在大多数视觉任务上被取代？
- 视觉基础模型的「可解释性」能否满足医疗/安全场景的需求？
- 扩散生成的版权、虚假信息、检测与水印如何平衡？
- 3D 与视频理解能否达到图像理解的成熟度？

### 稳定参考

- 深度专题（多模态部分）：[`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)
- 对应卡片：[`cards/18-computer-vision.md`](../cards/18-computer-vision.md)

## 智能体联网增量区（动态，带日期戳）

> 以下由智能体联网检索补充，每条须标注检索日期与来源链接，未经人工审校。引用前核实原始论文/官方公告。
> 写入约定见 [`opencode/AGENTS.md`](../../opencode/AGENTS.md)。

- _（待智能体联网补充：新模型、新基准、生成与检测对抗、医学影像 AI 进展等）_

## 给学生的提示

- 视觉前沿更新快，注意区分「刷榜数字」与「实际可用」。
- 医学影像相关进展，务必回到临床验证与监管（如 FDA/NMPA）口径判断成熟度。
