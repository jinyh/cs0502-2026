"""CS0502 温度计数：可在 PAI-DSW 中运行；只用 Python 标准库。"""
import json


def count_alerts(readings, threshold):
    count = 0
    for temperature in readings:
        if temperature >= threshold:
            count = count + 1
    return count


def verify():
    cases = [([65, 81], 80, 1), ([80], 80, 1), ([], 80, 0), ([65, 80, 81], 80, 2), ([65, 80, 81], 81, 1)]
    results = []
    for readings, threshold, expected in cases:
        actual = count_alerts(readings, threshold)
        assert actual == expected, (readings, threshold, actual)
        results.append({"readings": readings, "threshold": threshold, "expected": expected, "actual": actual})
    assert sum(t > 80 for t in [65, 80, 81]) == 1
    return results


if __name__ == "__main__":
    readings = [65, 80, 81]
    print(count_alerts(readings, 80))
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
    print("空记录返回 0：没有记录，不代表设备正常。")
