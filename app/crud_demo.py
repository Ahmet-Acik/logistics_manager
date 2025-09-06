# # app/crud_demo.py
# from app.database import SessionLocal
# from app.models import Customer, Warehouse, Route, Shipment, Tracking, Inventory, ShipmentStatusHistory, Driver, Vehicle, User
# from datetime import datetime
#
# def create_customer(session, name, email, phone=None):
#     customer = Customer(name=name, email=email, phone=phone)
#     session.add(customer)
#     session.commit()
#     return customer
#
# def get_customers(session):
#     return session.query(Customer).all()
#
# def update_customer(session, customer_id, **kwargs):
#     customer = session.query(Customer).get(customer_id)
#     if not customer:
#         return None
#     for key, value in kwargs.items():
#         setattr(customer, key, value)
#     session.commit()
#     return customer
#
# def delete_customer(session, customer_id):
#     customer = session.query(Customer).get(customer_id)
#     if not customer:
#         return False
#     session.delete(customer)
#     session.commit()
#     return True
#
# def create_warehouse(session, name, location):
#     warehouse = Warehouse(name=name, location=location)
#     session.add(warehouse)
#     session.commit()
#     return warehouse
#
# def get_warehouses(session):
#     return session.query(Warehouse).all()
#
# def update_warehouse(session, warehouse_id, **kwargs):
#     warehouse = session.query(Warehouse).get(warehouse_id)
#     if not warehouse:
#         return None
#     for key, value in kwargs.items():
#         setattr(warehouse, key, value)
#     session.commit()
#     return warehouse
#
# def delete_warehouse(session, warehouse_id):
#     warehouse = session.query(Warehouse).get(warehouse_id)
#     if not warehouse:
#         return False
#     session.delete(warehouse)
#     session.commit()
#     return True
#
# def create_route(session, origin, destination, distance_km):
#     route = Route(origin=origin, destination=destination, distance_km=distance_km)
#     session.add(route)
#     session.commit()
#     return route
#
# def get_routes(session):
#     return session.query(Route).all()
#
# def update_route(session, route_id, **kwargs):
#     route = session.query(Route).get(route_id)
#     if not route:
#         return None
#     for key, value in kwargs.items():
#         setattr(route, key, value)
#     session.commit()
#     return route
#
# def delete_route(session, route_id):
#     route = session.query(Route).get(route_id)
#     if not route:
#         return False
#     session.delete(route)
#     session.commit()
#     return True
#
# def create_shipment(session, customer_id, warehouse_id, route_id, status='pending'):
#     shipment = Shipment(
#         customer_id=customer_id,
#         warehouse_id=warehouse_id,
#         route_id=route_id,
#         status=status,
#         created_at=datetime.now(),
#         updated_at=datetime.now()
#     )
#     session.add(shipment)
#     session.commit()
#     return shipment
#
# def get_shipments(session):
#     return session.query(Shipment).all()
#
# def update_shipment(session, shipment_id, **kwargs):
#     shipment = session.query(Shipment).get(shipment_id)
#     if not shipment:
#         return None
#     for key, value in kwargs.items():
#         setattr(shipment, key, value)
#     shipment.updated_at = datetime.now()
#     session.commit()
#     return shipment
#
# def delete_shipment(session, shipment_id):
#     shipment = session.query(Shipment).get(shipment_id)
#     if not shipment:
#         return False
#     session.delete(shipment)
#     session.commit()
#     return True
#
# def create_tracking(session, shipment_id, status, location):
#     tracking = Tracking(
#         shipment_id=shipment_id,
#         status=status,
#         location=location,
#         timestamp=datetime.now()
#     )
#     session.add(tracking)
#     session.commit()
#     return tracking
#
# def get_trackings(session):
#     return session.query(Tracking).all()
#
# def update_tracking(session, tracking_id, **kwargs):
#     tracking = session.query(Tracking).get(tracking_id)
#     if not tracking:
#         return None
#     for key, value in kwargs.items():
#         setattr(tracking, key, value)
#     session.commit()
#     return tracking
#
# def delete_tracking(session, tracking_id):
#     tracking = session.query(Tracking).get(tracking_id)
#     if not tracking:
#         return False
#     session.delete(tracking)
#     session.commit()
#     return True
#
# def create_inventory(session, warehouse_id, item_name, quantity):
#     from datetime import datetime
#     inventory = Inventory(
#         warehouse_id=warehouse_id,
#         item_name=item_name,
#         quantity=quantity,
#         last_updated=datetime.now()
#     )
#     session.add(inventory)
#     session.commit()
#     return inventory
#
# def get_inventories(session):
#     return session.query(Inventory).all()
#
# def update_inventory(session, inventory_id, **kwargs):
#     from datetime import datetime
#     inventory = session.query(Inventory).get(inventory_id)
#     if not inventory:
#         return None
#     for key, value in kwargs.items():
#         setattr(inventory, key, value)
#     inventory.last_updated = datetime.now()
#     session.commit()
#     return inventory
#
# def delete_inventory(session, inventory_id):
#     inventory = session.query(Inventory).get(inventory_id)
#     if not inventory:
#         return False
#     session.delete(inventory)
#     session.commit()
#     return True
#
# def create_shipment_status_history(session, shipment_id, status):
#     from datetime import datetime
#     history = ShipmentStatusHistory(
#         shipment_id=shipment_id,
#         status=status,
#         timestamp=datetime.now()
#     )
#     session.add(history)
#     session.commit()
#     return history
#
# def get_shipment_status_histories(session, shipment_id=None):
#     query = session.query(ShipmentStatusHistory)
#     if shipment_id:
#         query = query.filter_by(shipment_id=shipment_id)
#     return query.all()
#
# def create_driver(session, name, phone=None, license_number=None):
#     driver = Driver(name=name, phone=phone, license_number=license_number)
#     session.add(driver)
#     session.commit()
#     return driver
#
# def get_drivers(session):
#     return session.query(Driver).all()
#
# def update_driver(session, driver_id, **kwargs):
#     driver = session.query(Driver).get(driver_id)
#     if not driver:
#         return None
#     for key, value in kwargs.items():
#         setattr(driver, key, value)
#     session.commit()
#     return driver
#
# def delete_driver(session, driver_id):
#     driver = session.query(Driver).get(driver_id)
#     if not driver:
#         return False
#     session.delete(driver)
#     session.commit()
#     return True
#
# def main():
#     session = SessionLocal()
#     # Example usage: create, read, update, delete for each model
#     # Add your own test cases here
#     session.close()
#
# if __name__ == "__main__":
#     main()
