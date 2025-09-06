from app.models import Customer
from sqlalchemy.exc import IntegrityError

def create_customer(session, name, email, phone=None):
    customer = Customer(name=name, email=email, phone=phone)
    session.add(customer)
    session.commit()
    try:
        session.commit()
        return customer
    except IntegrityError:
        session.rollback()
        return None
    customer = session.query(Customer).get(customer_id)
    if not customer:
        return None
    for key, value in kwargs.items():
        setattr(customer, key, value)
    session.commit()
    return customer

def delete_customer(session, customer_id):
    customer = session.query(Customer).get(customer_id)
    if not customer:
        return False
    session.delete(customer)
    session.commit()
    return True

def get_customers(session):
    return session.query(Customer).all()

def update_customer(session, customer_id, **kwargs):
    customer = session.query(Customer).get(customer_id)
    if not customer:
        return None
    for key, value in kwargs.items():
        setattr(customer, key, value)
    session.commit()
    return customer

