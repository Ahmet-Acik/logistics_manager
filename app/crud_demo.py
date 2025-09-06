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

def create_warehouse(session, name, location):
    warehouse = Warehouse(name=name, location=location)
    session.add(warehouse)
    session.commit()
    return warehouse

def get_warehouses(session):
    return session.query(Warehouse).all()

def update_warehouse(session, warehouse_id, **kwargs):
    warehouse = session.query(Warehouse).get(warehouse_id)
    for key, value in kwargs.items():
        setattr(warehouse, key, value)
    session.commit()
    return warehouse

def delete_warehouse(session, warehouse_id):
    warehouse = session.query(Warehouse).get(warehouse_id)
    session.delete(warehouse)
    session.commit()

def create_route(session, origin, destination, distance_km):
    route = Route(origin=origin, destination=destination, distance_km=distance_km)
    session.add(route)
    session.commit()
    return route

def get_routes(session):
    return session.query(Route).all()

def update_route(session, route_id, **kwargs):
    route = session.query(Route).get(route_id)
    for key, value in kwargs.items():
        setattr(route, key, value)
    session.commit()
    return route

def delete_route(session, route_id):
    route = session.query(Route).get(route_id)
    session.delete(route)
    session.commit()

def create_shipment(session, customer_id, warehouse_id, route_id, status='pending'):
    shipment = Shipment(
        customer_id=customer_id,
        warehouse_id=warehouse_id,
        route_id=route_id,
        status=status,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    session.add(shipment)
    session.commit()
    return shipment

def get_shipments(session):
    return session.query(Shipment).all()

def update_shipment(session, shipment_id, **kwargs):
    shipment = session.query(Shipment).get(shipment_id)
    for key, value in kwargs.items():
        setattr(shipment, key, value)
    shipment.updated_at = datetime.now()
    session.commit()
    return shipment

def delete_shipment(session, shipment_id):
    shipment = session.query(Shipment).get(shipment_id)
    session.delete(shipment)
    session.commit()




def main():
    session = SessionLocal()
    # Example usage: create, read, update, delete for each model
    # Add your own test cases here
    session.close()

if __name__ == "__main__":
    main()
