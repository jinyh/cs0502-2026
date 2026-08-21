"""Slide08：显式状态、纸带、读写头和转移表的图灵机模拟器。"""


def run_machine(transitions, input_text, start="scan", halt="halt", max_steps=100):
    tape = {index: symbol for index, symbol in enumerate(input_text)}
    state, head, trace = start, 0, []
    for step in range(max_steps + 1):
        trace.append((step, state, head, tape.get(head, "_")))
        if state == halt:
            break
        if step == max_steps:
            raise TimeoutError("超过最大步数，机器可能不会停机")
        symbol = tape.get(head, "_")
        rule = transitions.get((state, symbol))
        if rule is None:
            raise ValueError(f"没有转移规则: state={state}, symbol={symbol}")
        state, written, direction = rule
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


if __name__ == "__main__":
    result, execution = run_machine(FLIP_BITS, "0110")
    print("输出:", result)
    print("执行轨迹:")
    for row in execution:
        print(row)
