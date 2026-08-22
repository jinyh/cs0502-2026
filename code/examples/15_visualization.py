"""Slide15：四种分析任务对应四类图。输出到 student-work/。"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


def configure_chinese_font():
    """优先选常见中文字体；无可用字体时仍可运行英文标签。"""
    for name in ("PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", "Arial Unicode MS"):
        try:
            font_manager.findfont(name, fallback_to_default=False)
        except ValueError:
            continue
        plt.rcParams["font.sans-serif"] = [name, "DejaVu Sans"]
        break
    plt.rcParams["axes.unicode_minus"] = False


def main():
    configure_chinese_font()
    rng = np.random.default_rng(42)
    time = np.arange(12)
    signal = 20 + 0.5 * time + rng.normal(0, 0.8, len(time))
    groups = [rng.normal(10, 1, 40), rng.normal(12, 1.5, 40)]

    figure, axes = plt.subplots(2, 2, figsize=(9, 6))
    axes[0, 0].plot(time, signal, marker="o")
    axes[0, 0].set_title("Trend / 趋势")
    axes[0, 0].set_xlabel("Month / 月")
    axes[0, 0].set_ylabel("Temperature / 温度 (°C)")
    axes[0, 1].hist(groups[0], bins=8)
    axes[0, 1].set_title("Distribution / 分布")
    axes[0, 1].set_xlabel("Strength / 强度 (MPa)")
    axes[0, 1].set_ylabel("Count / 样本数")
    axes[1, 0].scatter(groups[0], groups[1])
    axes[1, 0].set_title("Relationship / 关系")
    axes[1, 0].set_xlabel("Input A / 输入 A")
    axes[1, 0].set_ylabel("Response B / 响应 B")
    axes[1, 1].boxplot(groups, tick_labels=["A", "B"])
    axes[1, 1].set_title("Comparison / 比较")
    axes[1, 1].set_xlabel("Material / 材料")
    axes[1, 1].set_ylabel("Strength / 强度 (MPa)")
    figure.tight_layout()

    output = Path("student-work/15-visualization.svg")
    output.parent.mkdir(exist_ok=True)
    figure.savefig(output)
    print("已保存:", output)


if __name__ == "__main__":
    main()
