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
    # Reconnect to the new DB for table creation
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    with db_engine.begin() as conn:
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(50) UNIQUE,
                email VARCHAR(100),
                is_active BOOLEAN DEFAULT 1
            )
        '''))
        print("Created users table.")
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20) DEFAULT NULL,
                address TEXT,
                city VARCHAR(50) DEFAULT NULL,
                state VARCHAR(50) DEFAULT NULL,
                zip_code VARCHAR(10) DEFAULT NULL,
                country VARCHAR(50) DEFAULT 'USA',
                created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY email (email),
                KEY idx_customer_email (email),
                KEY idx_customer_name (last_name, first_name)
            )
        '''))
        print("Created customers table.")
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INT PRIMARY KEY AUTO_INCREMENT,
                product_name VARCHAR(200) NOT NULL,
                description TEXT,
                category_id INT DEFAULT NULL,
                price DECIMAL(10,2) NOT NULL,
                stock_quantity INT DEFAULT 0,
                sku VARCHAR(50) DEFAULT NULL,
                is_active TINYINT(1) DEFAULT 1,
                created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY sku (sku),
                KEY idx_product_name (product_name),
                KEY idx_category (category_id),
                KEY idx_price (price),
                KEY idx_product_sku (sku)
                -- Add FK constraint if categories table exists
            )
        '''))
        print("Created products table.")
        conn.execute(text('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INT PRIMARY KEY AUTO_INCREMENT,
                customer_id INT NOT NULL,
                order_date TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                status ENUM('pending','processing','shipped','delivered','cancelled') DEFAULT 'pending',
                total_amount DECIMAL(10,2) NOT NULL,
                shipping_address TEXT,
                billing_address TEXT,
                notes TEXT,
                KEY idx_customer (customer_id),
                KEY idx_order_date (order_date),
                KEY idx_status (status),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
            )
        '''))
        print("Created orders table.")
    print("Database and tables created.")

# DML: Insert, update, delete, select data
def dml_operations():
    db_engine = create_engine('mysql+mysqldb://root:root7623@localhost:3306/practice_db')
    with db_engine.begin() as conn:
        # Best Practice: Insert parent rows before child rows
        conn.execute(text("INSERT IGNORE INTO users (username, email) VALUES (:u, :e)"), {"u": "alice", "e": "alice@example.com"})
        conn.execute(text("INSERT IGNORE INTO products (product_name, price) VALUES (:n, :p)"), {"n": "Laptop", "p": 1200.00})
        # Insert a customer if not exists (since orders references customers)
        conn.execute(text("INSERT IGNORE INTO customers (customer_id, first_name, last_name, email) VALUES (1, 'Test', 'Customer', 'test@example.com')"))
        conn.execute(text("INSERT IGNORE INTO orders (customer_id, order_date, total_amount) VALUES (1, NOW(), 1200.00)"))
        # Best Practice: Use parameterized queries for updates
        conn.execute(text("UPDATE users SET is_active = 0 WHERE username = :u"), {"u": "alice"})
        # Best Practice: Use parameterized queries for deletes
        conn.execute(text("DELETE FROM products WHERE product_name = :n"), {"n": "Laptop"})
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
