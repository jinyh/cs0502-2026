---
title: 强化学习深度专题
aliases: [强化学习, RL, MDP, Q-learning, PPO, RLHF, 探索-利用]
category: ai-ml
tags: [强化学习, MDP, Q-learning, Policy-Gradient, PPO, RLHF, exploration]
status: needs-review
version: 1.1
importance: 4
authoritative_cards: [16-artificial-intelligence, 17-machine-learning]
related_frontier: []
last_reviewed: 2026-08-22
---

# 强化学习深度专题（Reinforcement Learning Deep Dive）

> 对应卡片：[`16-artificial-intelligence`](../cards/16-artificial-intelligence.md)、[`17-machine-learning`](../cards/17-machine-learning.md)
> 关联贪心：[`07-greedy-algorithm`](../cards/07-greedy-algorithm.md) 的 $\epsilon$-greedy 是对纯贪心的修正

强化学习（Reinforcement Learning, RL）研究 agent 在环境里通过试错、最大化累计奖励来学习策略。它与监督学习不同——没有「标准答案」，只有延迟的反馈信号。

## 1. 核心框架：MDP

马尔可夫决策过程（Markov Decision Process, MDP）$\langle S, A, P, R, \gamma\rangle$：
- 状态集 $S$、动作集 $A$、转移 $P(s'\mid s,a)$、奖励 $R$、折扣 $\gamma\in[0,1)$。
- 马尔可夫性：未来只依赖当前状态，与历史无关。
- 目标：找策略 $\pi(a\mid s)$ 最大化期望折扣回报 $J=\mathbb{E}\left[\sum_t \gamma^t r_t\right]$。
- 直觉：下棋——只看当前棋局决定怎么走，奖励是最后输赢。

$\gamma$ 控制「近视 vs 远视」：$\gamma\to0$ 只看眼前，$\gamma\to1$ 长远规划。

## 2. 价值函数与贝尔曼方程

- 状态价值 $V^\pi(s)=\mathbb{E}_\pi\left[\sum_t\gamma^t r_t\mid s_0=s\right]$。
- 动作价值 $Q^\pi(s,a)$：在 $s$ 做 $a$ 后的期望回报。
- 贝尔曼方程（递归关系）：

$$Q^\pi(s,a)=\mathbb{E}_{s'\sim P,\,a'\sim\pi}\left[r+\gamma\,Q^\pi(s',a')\right]$$

这是 RL 一切算法的根——把长期回报拆成「立即奖励 + 后续价值」。

## 3. 主要方法谱系

### 3.1 基于价值（value-based）

学 $Q$，再贪心选动作。代表 Q-learning：
$$Q(s,a)\leftarrow Q(s,a)+\alpha\left[r+\gamma\max_{a'}Q(s',a')-Q(s,a)\right]$$

Deep Q-Network（DQN, 2015）用神经网络估计 $Q$，并用经验回放与目标网络改善训练稳定性；论文在 Atari 基准中的许多游戏上达到或超过当时的人类基准，不能外推为一般环境中的“超人智能”。

### 3.2 基于策略（policy-based）

直接参数化 $\pi_\theta(a\mid s)$，用梯度上升最大化回报：

$$\nabla J\propto\mathbb{E}\left[\nabla_\theta\log\pi_\theta(a\mid s)\,G_t\right]$$

方差大，需基线（REINFORCE with baseline、Actor-Critic）。

### 3.3 Actor-Critic

同时学策略（actor）与价值（critic）：actor 出动作，critic 评价并给优势（advantage）信号。A2C/A3C/PPO 都属此类。

### 3.4 PPO（Proximal Policy Optimization）

PPO 通过限制新旧策略差异来减少过大更新，是广泛使用的策略优化基线，也曾被用于许多 RLHF 系统。它不是所有任务的默认最优算法，偏好优化还包括 DPO 等不显式运行强化学习的方法。

## 4. 探索-利用困境

- 利用（exploitation）：选当前最优——短期好但可能陷局部最优。
- 探索（exploration）：尝试未知——短期差但发现更优。
- $\epsilon$-greedy：以 $1-\epsilon$ 贪心、$\epsilon$ 随机——这正是 [`07`](../cards/07-greedy-algorithm.md) 贪心的修正版。
- Upper Confidence Bound（UCB）、好奇心驱动等更精巧的探索策略。

## 5. 与 LLM 的交汇：RLHF

RLHF（Reinforcement Learning from Human Feedback）把 RL 用于对齐大模型：
1. 从预训练基座模型出发，经 SFT 得到指令模型。
2. 训奖励模型 $r_\phi(s,a)$ 拟合人类偏好。
3. 用 PPO 优化 LLM 策略，最大化 $r_\phi$，同时加 KL 惩罚防止偏离 SFT 太远（对齐税）。

RLHF 把人类偏好转换为可优化的训练信号，是现代指令模型后训练的一条重要路线；具体产品能力还共同取决于预训练数据、模型、工程、评测与安全流程。详见 [`llm-deep-dive.md`](llm-deep-dive.md) 第 3.2 节。

## 6. 局限与前沿

- **样本效率低**：RL 常需千万次试错，现实（医疗/控制）难承受。离线 RL、模仿学习缓解。
- **奖励设计难**：错误奖励导致 reward hacking（agent 钻空子而非完成任务）。
- **稀疏奖励**：很多步后才有信号（如下棋输赢），credit assignment 难。
- **泛化**：仿真训练到现实有 sim-to-real gap。
- **安全 RL**：约束动作不越界（医疗/自动驾驶）。
- 前沿：RLHF 之外出现 DPO 等免 RL 方法；世界模型（world model）学环境模型提升样本效率。

## 7. 跨学科联系

- **与心理学/神经科学**：RL 的奖励信号与多巴胺、强化学习理论本身源于行为主义。
- **与控制论**：最优控制与 RL 是「决定 vs 学习」的两面。
- **与医学**：个性化治疗可建模为 RL（状态=病情、动作=方案、奖励=预后），但伦理与样本成本限制其直接应用。
- **与博弈论**：多 agent RL 即学习型博弈。

## 8. 直觉类比

| 概念 | 类比 |
|---|---|
| MDP | 棋局：当前棋盘+合法走法+转移规则+输赢奖励 |
| 折扣 $\gamma$ | 重视眼前奖金还是长期养老金 |
| 贝尔曼方程 | 「今天的好日子 = 今天收入 + 对明天的期望」 |
| 探索-利用 | 餐厅：常去招牌（利用）还是试新店（探索） |
| reward hacking | 学生发现「只写关键词就能得分」于是不写完整答案 |

## 延伸阅读

- 经典教材：Sutton, R. & Barto, A. (2018). *Reinforcement Learning: An Introduction*, 2nd ed.（在线免费）
- DQN：Mnih, V. et al. (2015). Human-level control through deep RL. *Nature*.
- PPO：Schulman, J. et al. (2017). Proximal Policy Optimization. arXiv:1707.06347.
- RLHF：Christiano, P. et al. (2017). Deep RL from Human Preferences. NeurIPS.
