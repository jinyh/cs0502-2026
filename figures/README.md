# 静态配图

本目录保存知识点卡片使用的 30 张自包含 SVG。它们用于帮助学生在阅读正文前先建立结构直觉，不替代定义、代码或可运行实验。

## 对应关系

- L02：`02-data-representation.svg`

- Slide03：`03-language-pipeline.svg`
- Slide04：`04-linear-storage.svg`
- Slide05：`05-stack-queue-recursion.svg`、`05-tree-heap.svg`、`05-complexity-growth.svg`
- Slide06：`06-bfs-dfs.svg`
- L06：`06-algorithm-strategies.svg`
- Slide07：`07-greedy-dijkstra.svg`
- Slide08：`08-turing-transition.svg`
- Slide09：`09-computer-os-layers.svg`、`09-process-concurrency.svg`
- Slide11：`11-network-encapsulation.svg`
- L10：`10-distributed-request.svg`
- L11：`11-reproducibility-chain.svg`
- Slide12：`12-public-key-signature.svg`
- L12：`12-ai-threat-model.svg`
- Slide13：`13-relational-query.svg`
- Slide14：`14-clustering-comparison.svg`
- L14：`14-data-lifecycle.svg`
- Slide15：`15-chart-selection.svg`
- L15：`15-base-rate.svg`
- L16：`16-human-ai-loop.svg`
- Slide17：`17-neural-learning.svg`
- Slide18：`18-convolution.svg`
- L18：`18-evaluation-pipeline.svg`
- Slide20：`20-rnn-asr.svg`
- Slide21：`21-language-model-evolution.svg`
- L20：`20-rag-agent-loop.svg`
- L21：`21-responsible-ai-system.svg`

## 制作约定

- 优先使用 SVG，避免依赖外部字体、脚本或网络资源。
- 每张图包含 `<title>` 与 `<desc>`，正文中的图注说明学生应观察的关系。
- 标签以中文为主，首次出现的关键术语附英文。
- 图只呈现一个主要关系；需要操作和逐步观察的内容放入 `code/visualizations/`。
- 新增配图后，同时更新对应卡片 frontmatter 的 `figures` 字段与本文件。
