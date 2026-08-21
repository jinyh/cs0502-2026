"""Slide13：用内存 SQLite 演示关系、键、连接和查询。"""

import sqlite3


def main():
    connection = sqlite3.connect(":memory:")
    connection.executescript(
        """
        CREATE TABLE sample(id INTEGER PRIMARY KEY, material TEXT NOT NULL);
        CREATE TABLE measurement(
            id INTEGER PRIMARY KEY,
            sample_id INTEGER NOT NULL REFERENCES sample(id),
            strength REAL NOT NULL
        );
        INSERT INTO sample VALUES (1, 'Alloy-A'), (2, 'Alloy-B');
        INSERT INTO measurement VALUES (1, 1, 315.0), (2, 1, 325.0), (3, 2, 280.0);
        """
    )
    query = """
        SELECT sample.material, AVG(measurement.strength) AS mean_strength
        FROM sample JOIN measurement ON sample.id = measurement.sample_id
        GROUP BY sample.id, sample.material
        ORDER BY mean_strength DESC
    """
    for material, mean_strength in connection.execute(query):
        print(material, round(mean_strength, 1))
    connection.close()


if __name__ == "__main__":
    main()
