"""L02：整数、浮点数、文本和量化的表示边界。仅使用标准库。"""


def wrap_unsigned(value, bits):
    """把整数限制到给定位宽，演示无符号回绕。"""
    return value % (2**bits)


def quantize_unit_interval(value, bits):
    """把 [0, 1] 测量值映射到包含两个端点的均匀等级。"""
    if not 0 <= value <= 1:
        raise ValueError("value 必须位于 [0, 1]")
    if bits < 1:
        raise ValueError("bits 必须至少为 1")
    max_code = 2**bits - 1
    code = int(value * max_code + 0.5)
    reconstructed = code / max_code
    return code, reconstructed


def main():
    print("0.1 + 0.2 =", repr(0.1 + 0.2))
    print("是否严格等于 0.3:", 0.1 + 0.2 == 0.3)
    print("8 位无符号 255 + 1:", wrap_unsigned(255 + 1, 8))

    text = "交大 A"
    encoded = text.encode("utf-8")
    print("字符数:", len(text), "UTF-8 字节数:", len(encoded))
    print("UTF-8 字节:", list(encoded))

    for measurement in (0.1, 0.5, 0.9):
        code, recovered = quantize_unit_interval(measurement, bits=2)
        print(f"测量 {measurement:.1f} -> 码字 {code:02b} -> 近似 {recovered:.3f}")


if __name__ == "__main__":
    main()
