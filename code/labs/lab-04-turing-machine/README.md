# 实验 04：图灵机

实现通用 `run_machine`：转移表的键是 `(state, symbol)`，值是 `(next_state, written_symbol, direction)`。返回输出和逐步轨迹，并用最大步数阻止无限运行。

先手工执行测试中的翻转机器。验收：显式记录状态、纸带、读写头；缺规则和超步数时给出不同错误。
