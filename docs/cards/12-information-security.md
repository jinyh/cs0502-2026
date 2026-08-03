---
title: 信息安全与密码学
lecture: Slide12-InformationSecurity-2025
aliases: [信息安全, 密码学, 对称加密, 公钥加密, 哈希, 网络安全]
thinking_pillar: 系统思维
category: networking-security
tags: [信息安全, 密码学, 对称加密, RSA, 哈希, 入门]
status: stable
version: 1.0
importance: 4
related_cards: [11-computer-network, 08-turing-machine]
related_deep: []
related_visualizations: []
last_reviewed: 2026-08-03
---

# 信息安全与密码学（Information Security & Cryptography）

> 对应讲稿：`Slide12-InformationSecurity-2025.pdf`（见课程 Canvas，不在公开仓库）

## 一句话定位

信息安全保障数据的**机密性、完整性、可用性**（CIA 三元组）。密码学是其工具箱：用数学把「信任」从「藏起来」变成「算不动」。

## 核心知识点

### CIA 三元组

- 机密性（confidentiality）：只有授权方能读。
- 完整性（integrity）：未被篡改。
- 可用性（availability）：需要时能用。

### 对称加密（symmetric）

加解密用同一密钥。如 AES。快，但密钥分发难。

### 公钥加密（asymmetric / public-key）

一对密钥：公钥公开、私钥保密。如 RSA、ECC。
- 加密：公钥加，私钥解。
- 签名：私钥签，公钥验。
- 解决了密钥分发问题，但慢——实务中用公钥协商对称密钥，再用对称加密通信（如 TLS）。

### 哈希函数

单向：把任意输入压成定长摘要。如 SHA-256。
- 用途：完整性校验、口令存储、区块链。
- 抗碰撞：难找到两个输入同摘要。
- 注意：哈希（非密钥）≠ 加密（密钥），混淆是常见误区（关联 `05`）。

### 数字签名

私钥对消息哈希签名，对方用公钥验证——同时保证来源真实与完整性。

### 安全威胁

钓鱼、中间人、重放、SQL 注入、侧信道。防御靠纵深（多层防护）而非单一手段。

## 直觉类比

| 概念 | 类比 |
|---|---|
| 对称密钥 | 同一把钥匙锁信箱，发收方各持一把（但怎么安全送钥匙？） |
| 公钥加密 | 公开信箱口（谁都能投），只有你有钥匙能开 |
| 数字签名 | 蜡封家徽：别人仿不出你的封印 |
| 哈希 | 指纹：不代表全文但能比对身份 |

## 前沿进展注记

- 量子计算威胁 RSA/ECC（Shor 算法）→ 后量子密码学（PQC）标准化进行中。
- 零知识证明（ZKP）、同态加密（在密文上计算）。
- 医疗数据：联邦学习 + 差分隐私做「可用不可见」。

## 跨学科联系

- 与数学：数论（RSA 基于大整数分解难）、椭圆曲线。
- 与医学：医疗数据隐私是 HIPAA/个保法核心；基因数据尤其敏感。
- 与计算理论：单向函数的存在性是未解难题（关联 `08`）。

## 推荐交互式问答

1. 对称与公钥加密各解决什么？为什么实际用两者结合？
2. 哈希和加密有什么区别？为什么口令要存哈希而非明文？
3. 量子计算为什么威胁 RSA？后量子密码在做什么？
4. 医院电子病历如何同时保证医生可用与患者隐私？

## 延伸阅读

- 对应讲稿 `Slide12-InformationSecurity-2025.pdf`。
- 关联：`11`（TLS 跑在网络上）、`08`（单向函数理论）。
- 经典：Katz, J. & Lindell, Y. (2020). *Introduction to Modern Cryptography*.
