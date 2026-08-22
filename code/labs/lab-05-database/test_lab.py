import sqlite3

from starter import create_schema, insert_measurements, strongest_materials


def test_relational_query():
    connection = sqlite3.connect(":memory:")
    create_schema(connection)
    insert_measurements(connection, [("A", 10.0), ("A", 14.0), ("B", 11.0)])
    assert strongest_materials(connection, 2) == [("A", 12.0), ("B", 11.0)]


def test_schema_constraints_and_tie_order():
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")
    create_schema(connection)
    insert_measurements(connection, [("B", 10.0), ("A", 10.0)])
    assert strongest_materials(connection, 10) == [("A", 10.0), ("B", 10.0)]
