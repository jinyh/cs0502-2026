---
title: 可重复计算、版本与证据链
card_id: reproducible-computing
lecture_refs: [L11, L14, L18, L21]
source_slides: [Slide10-SoftwareEngineering-2025, Slide14-DataMining-2025]
aliases: [可重复性, 版本控制, 实验记录, 数据版本, 随机种子]
thinking_pillars: [系统思维, 数据思维]
category: software-engineering
tags: [Git, 版本, 环境, 数据来源, 参数, 随机种子, 测试, 可重复性]
status: needs-review
version: 1.0
importance: 5
learning_objectives: [区分重复复现与复核, 记录最小实验清单, 为结果建立主张到证据链]
prerequisites: [10-software-engineering, ext-scientific-computing]
estimated_minutes: 35
assessment_tags: [实验设计, 证据审查, 版本追踪, 项目复盘]
labs: []
figures: [11-reproducibility-chain.svg]
related_cards: [10-software-engineering, ext-scientific-computing, data-lifecycle-governance, ml-evaluation, responsible-ai-systems]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-21
---

# 可重复计算、版本与证据链（Reproducible Computing）

> 新课程位置：L11；为数据分析、机器学习和课程项目提供共同的工程证据标准。

## 一句话定位

可信结果不只是一个数字，而是一条可追溯链：谁用哪一版代码、数据、环境和参数，通过什么步骤得到它，又用什么独立证据检查它。

![可重复计算证据链](../../figures/11-reproducibility-chain.svg)

## 学完应能做到

1. 区分重复运行（repeatability）、独立复现（reproducibility）和结论复核（replicability）的关注点。
2. 为一次计算实验记录代码、数据、环境、参数、随机性、命令和评价版本。
3. 用“主张—证据—限制”审查项目结果，而不是只看最终图表或模型分数。

## 核心知识点

### 最小可重复清单

- **代码**：提交哈希或发布版本，以及实际执行入口。
- **数据**：来源、许可、获取日期、不可变版本或校验摘要；敏感数据不能因此公开。
- **环境**：语言、依赖、操作系统及必要硬件信息，使用锁文件而非模糊的“最新版本”。
- **配置**：参数、预处理、单位、随机种子和数据划分。
- **执行**：命令、日志、退出状态和生成物位置。
- **评价**：指标定义、测试集版本、基线和不确定性。

### Git 记录变更，不自动证明正确

- 一个提交应表达一个可解释变化，并配合测试或文档说明。
- 分支帮助隔离工作，代码评审帮助发现假设；二者都不能替代领域验证。
- 大数据集和凭据不应直接进入公开 Git；应保存安全位置和可追溯标识。

### 随机种子只是一个条件

- 固定种子能复现伪随机序列，但库版本、硬件、并行顺序和非确定算子仍可能改变结果。
- 报告多个种子或置信区间，比挑选一次最好结果更可信。
- 真正目标是让差异可解释，而不是强迫所有平台逐位相同。

### 主张必须匹配证据

- 单元测试支持“函数在这些条件下行为正确”。
- 留出测试支持“模型在这一采样分布上达到某指标”。
- 它们都不能单独支持“系统在所有真实用户和未来环境中可靠”。

## 工程桥接

- 材料仿真结果需要网格、边界条件、求解器版本和误差准则。
- 医学模型除了代码，还需要数据纳入标准、伦理授权和群体分层证据。
- AI 生成代码应保留提示或任务规格、人工修改和独立测试，但不应把敏感输入提交到公开仓库。

## 常见误区与边界

- “能在我的机器运行”不等于他人能复现。
- “固定随机种子”不等于实验设计正确或结论稳定。
- “容器化”封装环境，不自动解决数据许可、硬件差异和错误规格。
- “提交了所有数据”可能违反隐私与版权；可追溯不等于必须公开。

## 主动学习与考核迁移

- **审计**：给一个只写“Python 3、运行 notebook”的实验说明，列出至少八个缺失信息。
- **版本**：解释为什么修改测试集后必须产生新评价版本，不能覆盖旧分数。
- **迁移**：为一个无法公开的医学数据项目设计“安全存储 + 数据版本标识 + 可重复脚本”方案。
- **项目证据**：每个主要结论写成“主张—直接证据—限制—复现命令”四列。

## 与课程图谱关系

- 软件测试见 [`10-software-engineering`](10-software-engineering.md)。
- 数值误差见 [`ext-scientific-computing`](ext-scientific-computing.md)。
- 数据来源和治理见 [`data-lifecycle-governance`](data-lifecycle-governance.md)。
- 模型评价见 [`ml-evaluation`](ml-evaluation.md)。

## 延伸阅读

- Wilson, G. et al. (2017). Good enough practices in scientific computing. *PLOS Computational Biology*.
- Sandve, G. K. et al. (2013). Ten simple rules for reproducible computational research. *PLOS Computational Biology*.
