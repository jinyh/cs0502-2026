def create_schema(connection):
    """在给定 SQLite connection 中创建 sample 与 measurement 约束表。"""
    raise NotImplementedError


def insert_measurements(connection, rows):
    """插入 (材料名, 强度) 行；同名材料复用 sample 记录。"""
    raise NotImplementedError


def strongest_materials(connection, limit=3):
    """返回平均强度最高的 (材料名, 平均值)，同分按名称升序。"""
    raise NotImplementedError
