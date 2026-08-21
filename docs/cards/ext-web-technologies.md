---
title: Web 技术基础
lecture: 扩展（无单独讲稿，参考 Harvard CS50 Web 模块）
aliases: [Web, HTTP, HTML, 前后端, REST, API]
thinking_pillar: 系统思维
category: networking-security
tags: [Web, HTTP, HTML, 前后端, REST, API, 入门]
status: needs-review
version: 1.0
importance: 3
related_cards: [11-computer-network, 12-information-security, 21-llm]
related_deep: [llm-deep-dive]
related_visualizations: []
last_reviewed: 2026-08-03
---

# Web 技术基础（Web Technologies）

> 扩展卡片：Harvard CS50 含 Web 模块；AI 时代前端与 LLM 接入是学生日常工具，21 讲未单独成讲。

## 一句话定位

Web 用一组开放协议（HTTP/HTML）把全球文档与应用连成可交互的整体。理解它的「前端-后端-协议」三层，是使用与搭建 AI 应用的基础。

## 核心知识点

### 客户端-服务器模型

- 浏览器（前端/client）发请求，服务器（后端/server）回响应。
- 跑在 [`11`](11-computer-network.md) 的 TCP/IP 之上，HTTP 是应用层协议。

### HTTP（HyperText Transfer Protocol）

- 请求方法：GET（取）、POST（交）、PUT/DELETE 等。
- 无状态（stateless）——每次请求独立，状态靠 cookie/session/token 维持。
- HTTPS = HTTP + TLS 加密（见 [`12`](12-information-security.md)）。

### 前端三件套

- **HTML**：内容结构（骨架）。
- **CSS**：样式表现（皮肤）。
- **JavaScript**：交互行为（肌肉）。
- 浏览器解析渲染这三者成你看到的页面。

### 后端与 API

- 后端处理业务逻辑、读写数据库（[`13`](13-database.md)）。
- **REST**：一种 API 设计风格，用 URL 路径定位资源、HTTP 方法表达动作、JSON 传数据。
- 前后端分离：前端只管渲染，通过 API 与后端通信。

### AI 时代的新角色

- LLM 常以 **API** 形式提供（OpenAI 兼容 endpoint，见 [`opencode/tools.md`](../../opencode/tools.md)）——Web 是人与 AI 交互的主通道。
- 前端从「展示」转向「对话/生成」：聊天界面、流式输出、工具调用结果渲染。
- RAG（检索增强生成）本质是 Web/API + 数据库 + LLM 的组合（见 [`21`](21-llm.md)）。

## 直觉类比

| 概念 | 类比 |
|---|---|
| HTTP 请求-响应 | 餐厅点单：菜单（URL）+ 点单（GET/POST）+ 上菜（response） |
| HTML/CSS/JS | 骨架/皮肤/肌肉 |
| REST API | 标准化的「窗口办事流程」——按规矩填表取号 |
| 无状态 | 每次去银行都要重新出示身份证（靠 token 维持身份） |

## 前沿进展注记

Web 基础稳定。AI 时代趋势：前端成为 LLM 对话界面，后端成为 Agent 工具编排层；Serverless 与边缘计算降低部署门槛。具体见 [`frontier/llm-frontier.md`](../frontier/llm-frontier.md)。

## 跨学科联系

- **与系统思维**：前后端分离是分层抽象的又一范例（关联 [`11`](11-computer-network.md)）。
- **与医学**：医院信息系统、远程问诊平台、可穿戴数据上传都建立在 Web 协议之上。
- **与工科**：工业物联网平台、船舶/航空航天遥测数据的 Web 可视化面板，都是「传感器→后端→前端图表」的同构。
- **与安全**：Web 是攻击主战场（XSS/CSRF/注入），见 [`12`](12-information-security.md)。

## 主动学习任务

1. 浏览器输入网址到看到页面，前后端各做了什么？（关联 [`11`](11-computer-network.md)）
2. HTTP 为什么是无状态的？怎么维持登录状态？
3. REST API 的「资源 + 方法 + JSON」为什么好？
4. LLM 为什么多以 Web API 形式提供？这降低了什么门槛？
5. 用「传感器→后端→前端」描述你专业里一个数据采集展示系统。

## 代码示例

```python
# 对应 docs/cards/ext-web-technologies；一个最简 HTTP 请求（概念演示）
# 运行需联网，沙箱内禁网——故此处仅作伪代码/概念演示，实际在本地跑
import json
# 真实调用（本地运行，非沙箱）：
# import urllib.request
# req = urllib.request.Request("https://httpbin.org/get")
# resp = urllib.request.urlopen(req).read().decode()
# print(json.loads(resp)["headers"])

# 概念：REST 风格
# GET    /patients/123       -> 取 id=123 的患者
# POST   /patients           -> 新建患者（body=JSON）
# PUT    /patients/123       -> 更新
# DELETE /patients/123       -> 删除
print("REST: 用 URL 定位资源，HTTP 方法表达动作，JSON 传数据")
```

## 延伸阅读

- 对照课程：Harvard CS50（Web track：HTML/CSS/Python/Flask/SQL）。
- 关联：[`11`](11-computer-network.md)（HTTP 跑在 TCP 上）、[`12`](12-information-security.md)（HTTPS/Web 安全）、[`21`](21-llm.md)（LLM API 接入）。
- 经典：Mozilla Developer Network (MDN) Web 文档。
