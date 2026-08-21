"""L09：枚举两个非原子“读—写”加一操作的合法交错。"""


def valid_schedules(prefix=(), remaining=("A-read", "A-write", "B-read", "B-write")):
    if not remaining:
        yield prefix
        return
    for event in remaining:
        task, action = event.split("-")
        if action == "write" and f"{task}-read" in remaining:
            continue
        next_remaining = tuple(item for item in remaining if item != event)
        yield from valid_schedules(prefix + (event,), next_remaining)


def execute(schedule):
    shared = 0
    local = {}
    for event in schedule:
        task, action = event.split("-")
        if action == "read":
            local[task] = shared
        else:
            shared = local[task] + 1
    return shared


def main():
    outcomes = {}
    for schedule in valid_schedules():
        outcomes.setdefault(execute(schedule), schedule)
    for result, example in sorted(outcomes.items()):
        print("最终计数:", result, "示例交错:", " → ".join(example))
    print("两个任务各加一，错误交错仍可能只得到 1。")


if __name__ == "__main__":
    main()
