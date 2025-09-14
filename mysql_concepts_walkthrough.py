"""
mysql_concepts_walkthrough.py
A script to demonstrate MySQL concepts: CREATE, ALTER, INSERT, UPDATE, DELETE, TRUNCATE, and DROP.
Each run starts from scratch for a clean demo.
"""
import sqlalchemy
from sqlalchemy import create_engine, text

# Update with your actual connection string
engine = create_engine('mysql+mysqldb://root:root7623@localhost/logistics_db')

with engine.connect() as conn:
    # Drop table if exists
    conn.execute(text("DROP TABLE IF EXISTS demo_table"))
    print("Dropped table if existed.")

    # CREATE TABLE
    conn.execute(text('''
        CREATE TABLE demo_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            value INT
        )
    '''))
    print("Created demo_table.")

    # INSERT
    conn.execute(text("INSERT INTO demo_table (name, value) VALUES ('Alice', 10), ('Bob', 20), ('Carol', 30)"))
    print("Inserted rows.")

    # SELECT
    result = conn.execute(text("SELECT * FROM demo_table"))
    print("Initial data:")
    for row in result:
        print(row)

    # UPDATE
    conn.execute(text("UPDATE demo_table SET value = value + 5 WHERE name = 'Alice'"))
    print("Updated Alice's value.")

    # SELECT after update
    result = conn.execute(text("SELECT * FROM demo_table"))
    print("After update:")
    for row in result:
        print(row)

    # DELETE
    conn.execute(text("DELETE FROM demo_table WHERE name = 'Bob'"))
    print("Deleted Bob.")

    # SELECT after delete
    result = conn.execute(text("SELECT * FROM demo_table"))
    print("After delete:")
    for row in result:
        print(row)

    # ALTER TABLE (add column)
    conn.execute(text("ALTER TABLE demo_table ADD COLUMN description VARCHAR(255) DEFAULT 'N/A'"))
    print("Added description column.")

    # UPDATE new column
    conn.execute(text("UPDATE demo_table SET description = 'Test row' WHERE name = 'Alice'"))
    print("Updated description for Alice.")

    # SELECT after alter
    result = conn.execute(text("SELECT * FROM demo_table"))
    print("After alter and update:")
    for row in result:
        print(row)

    # TRUNCATE TABLE
    conn.execute(text("TRUNCATE TABLE demo_table"))
    print("Truncated table.")

    # SELECT after truncate
    result = conn.execute(text("SELECT * FROM demo_table"))
    print("After truncate (should be empty):")
    for row in result:
        print(row)

    # DROP TABLE
    conn.execute(text("DROP TABLE demo_table"))
    print("Dropped demo_table.")
