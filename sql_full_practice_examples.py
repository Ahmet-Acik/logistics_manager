"""
sql_full_practice_examples.py

Comprehensive SQL practice examples for DDL, DML, DCL, and TCL operations using SQLAlchemy and pandas.
Each example uses real-world scenarios and includes comments to illustrate best practices.
A new database (practice_db) is created for demonstration.
"""

import pandas as pd
from sqlalchemy import create_engine, text

# Best Practice: Never hardcode credentials in production; use environment variables or config files
engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/')

# Utility function for displaying results
def show_df(df, title=None):
    if title:
        print(f"\n=== {title} ===")
    print(df.head())

# DDL: Create a new database and tables
def create_database_and_tables():
    # Best Practice: Use IF NOT EXISTS for idempotency
    with engine.begin() as conn:
        conn.execute(text('CREATE DATABASE IF NOT EXISTS practice_db;'))
        conn.execute(text('USE practice_db;'))
        # Best Practice: Execute DDL one statement at a time for compatibility
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE,
                email VARCHAR(100),
                is_active BOOLEAN DEFAULT 1
            );
        '''))
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS products (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100),
                price DECIMAL(10,2)
            );
        '''))
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS orders (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT,
                order_date DATE,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        '''))
    print("Database and tables created.")

# DML: Insert, update, delete, select data
def dml_operations():
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    with db_engine.begin() as conn:
        # Best Practice: Insert parent rows before child rows
        conn.execute(text("INSERT IGNORE INTO users (username, email) VALUES (:u, :e)"), {"u": "alice", "e": "alice@example.com"})
        conn.execute(text("INSERT IGNORE INTO products (name, price) VALUES (:n, :p)"), {"n": "Laptop", "p": 1200.00})
        conn.execute(text("INSERT IGNORE INTO orders (user_id, order_date) VALUES (1, NOW())"))
        # Best Practice: Use parameterized queries for updates
        conn.execute(text("UPDATE users SET is_active = 0 WHERE username = :u"), {"u": "alice"})
        # Best Practice: Use parameterized queries for deletes
        conn.execute(text("DELETE FROM products WHERE name = :n"), {"n": "Laptop"})
    # Best Practice: Use SELECT with explicit columns
    df = pd.read_sql('SELECT id, username, email, is_active FROM users;', db_engine)
    show_df(df, "Users Table After DML")

# TCL: Transaction control (COMMIT, ROLLBACK)
def tcl_transaction_example():
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    try:
        with db_engine.begin() as conn:
            # Best Practice: Use transactions for atomic multi-step changes
            conn.execute(text("INSERT INTO users (username, email) VALUES ('bob', 'bob@example.com')"))
            # Simulate error to trigger rollback
            raise Exception("Simulated error for rollback demo")
            conn.execute(text("INSERT INTO products (name, price) VALUES ('Tablet', 500.00)"))
    except Exception as e:
        print(f"Transaction rolled back due to: {e}")
    # Check that no partial data was inserted
    df = pd.read_sql('SELECT * FROM users WHERE username = "bob";', db_engine)
    show_df(df, "Users Table After Rollback")

# DCL: Grant and revoke privileges (requires admin rights)
def dcl_grant_revoke_example():
    # Best Practice: Use least privilege principle
    with engine.begin() as conn:
        # Grant SELECT on practice_db.users to a demo user
        conn.execute(text("GRANT SELECT ON practice_db.users TO 'demo_user'@'localhost';"))
        # Revoke SELECT
        conn.execute(text("REVOKE SELECT ON practice_db.users FROM 'demo_user'@'localhost';"))
    print("Granted and revoked SELECT privilege for demo_user.")

# Best Practice: Use EXPLAIN to analyze queries
def explain_query():
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    query = 'EXPLAIN SELECT * FROM orders WHERE user_id = 1;'
    df = pd.read_sql(query, db_engine)
    show_df(df, "EXPLAIN Orders Query")
    # Best Practice: Add indexes for performance (uncomment to use)
    # with db_engine.begin() as conn:
    #     conn.execute(text('CREATE INDEX idx_orders_user_id ON orders(user_id);'))

# Best Practice: Use CTEs for complex queries
def cte_example():
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    query = '''
    WITH user_orders AS (
        SELECT u.id, u.username, COUNT(o.id) AS order_count
        FROM users u
        LEFT JOIN orders o ON u.id = o.user_id
        GROUP BY u.id, u.username
    )
    SELECT * FROM user_orders WHERE order_count > 0;
    '''
    df = pd.read_sql(query, db_engine)
    show_df(df, "Users with Orders (CTE Example)")

if __name__ == "__main__":
    create_database_and_tables()
    dml_operations()
    tcl_transaction_example()
    dcl_grant_revoke_example()
    explain_query()
    cte_example()
