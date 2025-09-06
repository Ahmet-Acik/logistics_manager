from app.models import Warehouse

def create_warehouse(session, name, location):
    warehouse = Warehouse(name=name, location=location)
    session.add(warehouse)
    session.commit()
    return warehouse

def get_warehouses(session):
    return session.query(Warehouse).all()

def update_warehouse(session, warehouse_id, **kwargs):
    warehouse = session.query(Warehouse).get(warehouse_id)
    if not warehouse:
        return None
    for key, value in kwargs.items():
        setattr(warehouse, key, value)
    session.commit()
    return warehouse

def delete_warehouse(session, warehouse_id):
    warehouse = session.query(Warehouse).get(warehouse_id)
    if not warehouse:
        return False
    session.delete(warehouse)
    session.commit()
    return True

