# 实验 05：关系数据库

使用标准库 `sqlite3`。完成 `create_schema(connection)`、`insert_measurements(connection, rows)` 和 `strongest_materials(connection, limit)`。

模式至少包含 `sample` 与 `measurement` 两表、主键、外键和非空约束。查询按平均强度降序，再按材料名升序，禁止依赖数据库偶然顺序。
