"""L08：用地址步长解释二维数组访问的空间局部性。"""


def row_major_indices(rows, columns):
    return [row * columns + column for row in range(rows) for column in range(columns)]


def column_major_traversal_of_row_major_array(rows, columns):
    return [row * columns + column for column in range(columns) for row in range(rows)]


def total_address_jump(indices):
    return sum(abs(current - previous) for previous, current in zip(indices, indices[1:]))


def main():
    rows, columns = 4, 6
    by_row = row_major_indices(rows, columns)
    by_column = column_major_traversal_of_row_major_array(rows, columns)
    print("按行访问地址:", by_row)
    print("按列访问地址:", by_column)
    print("按行总地址跳跃:", total_address_jump(by_row))
    print("按列总地址跳跃:", total_address_jump(by_column))
    print("地址更连续通常意味着更好的空间局部性；实际性能仍需在目标机器实测。")


if __name__ == "__main__":
    main()
