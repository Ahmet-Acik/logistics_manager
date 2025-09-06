# app/create_tables.py
from app.models import Base
from app.database import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("All tables created.")
