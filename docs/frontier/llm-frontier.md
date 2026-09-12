---
topic: LLM
last_static_review: 2026-08-22
authoritative_card: 21-llm.md
deep_dive: llm-deep-dive.md
status: living
review_status: approved
ai_reviewed_at: 2026-08-22
human_reviewer: 课程负责人
human_reviewed_at: 2026-08-22
human_review_scope: [静态研究基线, 一手来源范围, 教学适切性]
---

# LLM 前沿进展注记

> 本页采用双层机制，详见 [`frontier/README.md`](README.md)。
> 静态层已由课程负责人审核通过；增量区未经审校。两层内容都不能替代学生回到原始论文核验。

## 静态写底层（季度检查）

### 静态研究基线

- **Transformer**：自注意力架构最初在序列转换任务中展示了并行训练优势，并成为后续语言模型的重要基础；这一结论不意味着所有现代模型结构完全相同。[Vaswani et al., NeurIPS 2017](https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- **检索增强生成（RAG）**：把参数化生成模型与外部非参数记忆结合，是“回答时引入可更新材料”的代表方法。是否提高事实性取决于检索召回、上下文组织、引用和端到端评测，不能把“用了 RAG”当成正确性证明。[Lewis et al., NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
- **偏好优化**：DPO 把一类带 KL 约束的偏好优化写成直接的分类式目标，避免单独训练奖励模型和在线采样；它是 RLHF 之外的重要路线，不表示在所有数据与任务上必然优于其他方法。[Rafailov et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html)
- **长上下文**：支持更长输入不等于能稳定利用其中每个位置的信息。受控实验显示，相关证据在上下文中的位置会显著影响部分模型表现。[Liu et al., TACL 2024](https://aclanthology.org/2024.tacl-1.9/)
- **工具与 Agent**：语言模型可以生成工具调用建议并利用返回结果，但权限、失败恢复、可观察性与验证属于外部系统责任。模型规模、产品名称、价格和上下文长度变化快，只进入带日期的增量区。

### 关键开放问题

- 如何分别测量事实错误、无依据陈述和引用错配，并判断哪些系统措施能稳定降低风险？
- 长上下文「迷失中段」如何缓解？
- 可授权、高质量数据的供给边界在哪里，合成数据何时改善学习、何时累积偏差？
- 涌现是真实现象还是评估指标的非线性？
- 推理时增加计算在哪些任务上稳定有效，如何避免把不可见内部过程当成可靠解释？

### 稳定参考

- 深度专题：[`deep/llm-deep-dive.md`](../deep/llm-deep-dive.md)

## 智能体联网增量区（动态，带日期戳）

> 以下由智能体联网检索补充，每条须标注检索日期与来源链接，未经人工审校。学生应批判性阅读，引用前核实原始论文/官方公告。
> 学生使用方式见 [OpenCode 学生使用指南](../student-guide.md)；写入约定保存在仓库维护文件 `opencode/AGENTS.md` 中。

- _（待智能体联网补充：新模型发布、能力评测、安全事件、研究突破等，每条一句话 + 来源 URL + 检索日期）_

## 给学生的提示

- 本页静态层是课程组批准基线，可用于课程学习和检索定位；作业或项目仍应引用对应的**原始论文 / 官方技术报告**，而不是引用本页概括。
- 增量区仅供参考与启发；产品能力或“最新”判断必须写明模型版本、评测条件和检索日期。
- 智能体若无法联网，本页仍以静态层为底，不阻塞学习。
