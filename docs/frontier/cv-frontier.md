---
topic: Computer Vision
last_static_review: 2026-08-22
authoritative_card: 18-computer-vision.md
deep_dive: null
status: living
review_status: approved
ai_reviewed_at: 2026-08-22
human_reviewer: 课程负责人
human_reviewed_at: 2026-08-22
human_review_scope: [静态研究基线, 一手来源范围, 教学适切性]
---

# 计算机视觉前沿进展注记

> 本页采用双层机制，详见 [`frontier/README.md`](README.md)。

## 静态写底层（季度检查）

> 本页静态层已由课程负责人审核通过；引用时仍应回到原论文核验实验范围。

### 静态研究基线

- **结构选择**：Vision Transformer 把图像切成 patch 序列并直接使用 Transformer，在其论文的预训练与迁移设置中取得有竞争力的结果。它并不证明 CNN 已被普遍替代；任务、数据量、算力和归纳偏置仍决定选择。[Dosovitskiy et al., ICLR 2021](https://arxiv.org/abs/2010.11929)
- **视觉—语言对齐**：CLIP 用图像—文本对比学习获得可迁移表示，并在论文评测中展示零样本迁移。零样本能力仍受训练数据、标签措辞、分布偏移和偏差影响。[Radford et al., ICML 2021](https://proceedings.mlr.press/v139/radford21a.html)
- **生成模型**：去噪扩散概率模型通过学习逆向去噪过程生成样本，奠定了重要的图像生成路线；“主导”“最好”等市场性判断必须限定日期、数据与指标。[Ho et al., NeurIPS 2020](https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html)
- **自监督视觉学习**：MAE 随机遮盖大比例图像 patch，以重建任务预训练编码器，论文显示了可扩展的表示学习结果。[He et al., CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper.html)
- **高风险应用**：医学影像等场景不能用单一数据集上的平均指标代替临床有效性。应报告外部验证、患者级划分、设备与人群分布、校准、失败模式和监管状态。

### 关键开放问题

- 基础模型与专用 CNN/ViT 在不同数据、时延、能耗和可解释性约束下如何组合？
- 视觉基础模型的「可解释性」能否满足医疗/安全场景的需求？
- 扩散生成的版权、虚假信息、检测与水印如何平衡？
- 3D 与视频方法如何在跨场景、动态对象和真实传感噪声下可靠泛化？

### 稳定参考

- 当前无课程组批准的专门 CV 深度专题；多模态基础见 [`cards/multimodal-models.md`](../cards/multimodal-models.md)。
- 对应卡片：[`cards/18-computer-vision.md`](../cards/18-computer-vision.md)

## 智能体联网增量区（动态，带日期戳）

> 以下由智能体联网检索补充，每条须标注检索日期与来源链接，未经人工审校。引用前核实原始论文/官方公告。
> 写入约定见 [`opencode/AGENTS.md`](../../opencode/AGENTS.md)。

- _（待智能体联网补充：新模型、新基准、生成与检测对抗、医学影像 AI 进展等）_

## 给学生的提示

- 视觉前沿更新快，注意区分「刷榜数字」与「实际可用」。
- 静态层是课程组批准基线，可用于课程学习和检索定位；作业或项目仍应引用原论文并说明实验范围。
- 医学影像相关进展，务必回到临床验证与监管（如 FDA/NMPA）口径判断成熟度。
