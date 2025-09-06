# config.py
# Update these values with your MySQL server credentials

DB_USER = 'root'
DB_PASSWORD = 'root7623'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'logistics_db'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
