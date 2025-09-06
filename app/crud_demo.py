# app/crud_demo.py
from app.database import SessionLocal
from app.models import Customer, Warehouse, Route, Shipment, Tracking
from datetime import datetime

def create_customer(session, name, email, phone=None):
    customer = Customer(name=name, email=email, phone=phone)
    session.add(customer)
    session.commit()
    return customer

def get_customers(session):
    return session.query(Customer).all()

def update_customer(session, customer_id, **kwargs):
    customer = session.query(Customer).get(customer_id)
    for key, value in kwargs.items():
        setattr(customer, key, value)
    session.commit()
    return customer

def delete_customer(session, customer_id):
    customer = session.query(Customer).get(customer_id)
    session.delete(customer)
    session.commit()




def main():
    session = SessionLocal()
    # Example usage: create, read, update, delete for each model
    # Add your own test cases here
    session.close()

if __name__ == "__main__":
    main()
