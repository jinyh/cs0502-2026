import sqlite3

from starter import create_schema, insert_measurements, strongest_materials


def test_relational_query():
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    insert_measurements(connection, [("A", 10.0), ("A", 14.0), ("B", 11.0)])
    assert strongest_materials(connection, 2) == [("A", 12.0), ("B", 11.0)]
