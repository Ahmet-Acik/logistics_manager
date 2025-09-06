from app.models import Inventory
from datetime import datetime

def create_inventory(session, warehouse_id, item_name, quantity):
    inventory = Inventory(
        warehouse_id=warehouse_id,
        item_name=item_name,
        quantity=quantity,
        last_updated=datetime.now()
    )
    session.add(inventory)
    session.commit()
    return inventory

def get_inventories(session):
    return session.query(Inventory).all()

def update_inventory(session, inventory_id, **kwargs):
    inventory = session.query(Inventory).get(inventory_id)
    if not inventory:
        return None
    for key, value in kwargs.items():
        setattr(inventory, key, value)
    inventory.last_updated = datetime.now()
    session.commit()
    return inventory

def delete_inventory(session, inventory_id):
    inventory = session.query(Inventory).get(inventory_id)
    if not inventory:
        return False
    session.delete(inventory)
    session.commit()
    return True

