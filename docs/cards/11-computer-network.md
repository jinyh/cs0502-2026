---
title: 计算机网络
lecture: Slide11-ComputerNetwork-2025
aliases: [网络, 分层, 协议, TCP/IP, HTTP]
thinking_pillar: 系统思维
category: networking-security
tags: [计算机网络, 分层, TCP/IP, HTTP, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [09-computer-system-arch, 12-information-security]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 计算机网络（Computer Network）

> 对应讲稿：[`Slide11-ComputerNetwork-2025.pdf`](../../LectureNotes/Slide11-ComputerNetwork-2025.pdf)

## 一句话定位

计算机网络用**分层协议**让全球异构机器互相通信。分层是系统思维的典范——每层只关心自己的职责，对上提供服务、对下使用服务。

## 核心知识点

### 为什么分层

- 异构：不同硬件、不同链路，需统一抽象。
- 分层把复杂问题拆成可管理的层：每层解决一个问题，向上提供接口。
- 类比：邮政系统分层（写信/邮递/运输），各层不关心上下层细节。

### OSI 七层 vs TCP/IP 四层

- TCP/IP 实用四层：链路 → 网络（IP）→ 传输（TCP/UDP）→ 应用（HTTP/SMTP/DNS）。
- OSI 七层是教学参考模型。

### 关键协议

- **IP**：网络层，负责寻址与路由——无连接、尽力交付。
- **TCP**：传输层，可靠、有序、面向连接（三次握手、流量/拥塞控制）。
- **UDP**：传输层，不可靠但快——视频、DNS。
- **HTTP**：应用层，Web 的基础协议（见 `03-web-technologies` 可选扩展）。
- **DNS**：域名解析，把名字变 IP。

### 数据封装

每层给数据加自己的头（header），层层包裹——接收方层层剥开。
- 直觉：信纸→信封→邮袋→集装箱，每层有自己的标签。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 分层 | 邮政：写信人只管写信，不管卡车怎么跑 |
| IP 路由 | 收件地址决定走哪条路 |
| TCP 可靠 | 挂号信，丢了重发、保证顺序 |
| DNS | 电话簿：名字→号码 |
| 分层封装 | 信纸套信封套邮袋 |

## 前沿进展注记

- 5G/6G、低延迟网络支撑实时应用。
- 内容分发网络（CDN）、边缘计算。
- 网络安全：零信任架构（关联 `12`）。

## 跨学科联系

- 与系统思维：分层是工程抽象的范例。
- 与医学：远程医疗、PACS 影像传输依赖可靠网络；IoT 医疗设备联网带来安全风险。
- 与信息论：带宽、延迟、吞吐的物理与数学约束（Shannon 极限）。

## 推荐交互式问答

1. 为什么要分层？不分层会怎样？
2. TCP 为什么比 UDP 可靠？可靠靠什么实现？
3. 输入网址到看到网页，发生了什么？（DNS→TCP→HTTP→渲染）
4. 医院影像传输用 TCP 还是 UDP？为什么？

## 延伸阅读

- 对应讲稿 `Slide11-ComputerNetwork-2025.pdf`。
- 关联：`12`（网络之上跑安全协议）、`09`（终端系统）。
- 经典：Kurose, J. & Ross, K. (2021). *Computer Networking: A Top-Down Approach*.
