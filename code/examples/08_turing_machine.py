"""2026 Slide07（原 Slide08）：单带图灵机翻转与一元加法，无第三方依赖。"""


def run_machine(transitions, input_text, start="scan", halt="halt", max_steps=100, *, start_head=0):
    tape = {index: symbol for index, symbol in enumerate(input_text)}
    state, head, trace = start, start_head, []
    for step in range(max_steps + 1):
        trace.append((step, state, head, tape.get(head, "_")))
        if state == halt:
            break
        if step == max_steps:
            raise TimeoutError("达到步数上限：本次未观察到停机")
        symbol = tape.get(head, "_")
        rule = transitions.get((state, symbol))
        if rule is None:
            raise ValueError(f"没有转移规则: state={state}, symbol={symbol}")
        state, written, direction = rule
        if direction not in {"L", "R"}:
            raise ValueError(f"不支持的移动方向: {direction}")
        tape[head] = written
        head += 1 if direction == "R" else -1
    left, right = min(tape, default=0), max(tape, default=0)
    output = "".join(tape.get(i, "_") for i in range(left, right + 1)).strip("_")
    return output, trace


FLIP_BITS = {
    ("scan", "0"): ("scan", "1", "R"),
    ("scan", "1"): ("scan", "0", "R"),
    ("scan", "_"): ("halt", "_", "R"),
}

# 一元编码：x 个 1、分隔符 0、y 个 1；▷ 和 ◁ 是边界符。
UNARY_ADDITION = {
    ("q1", "1"): ("q1", "1", "R"),
    ("q1", "0"): ("q2", "1", "R"),
    ("q2", "1"): ("q2", "1", "R"),
    ("q2", "◁"): ("q3", "_", "L"),
    ("q3", "1"): ("halt", "◁", "R"),
}


def run_unary_addition(x, y):
    """返回加法数值结果及轨迹；头从起始符右边的位置 1 开始。"""
    if type(x) is not int or type(y) is not int or x < 0 or y < 0:
        raise ValueError("一元加法的输入必须是非负整数")
    encoded = "▷" + "1" * x + "0" + "1" * y + "◁"
    output, trace = run_machine(
        UNARY_ADDITION, encoded, start="q1", start_head=1, max_steps=x + y + 3
    )
    return output.count("1"), trace


if __name__ == "__main__":
    result, execution = run_machine(FLIP_BITS, "0110")
    print("输出:", result)
    print("执行轨迹:")
    for row in execution:
        print(row)
    for x, y in [(3, 4), (0, 4), (4, 0), (0, 0)]:
        total, execution = run_unary_addition(x, y)
        print(f"一元加法 {x}+{y}={total}，转移 {len(execution) - 1} 次")
        if (x, y) == (3, 4):
            for row in execution:
                print(row)
