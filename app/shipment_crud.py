from app.models import Shipment
from datetime import datetime

def create_shipment(session, customer_id, warehouse_id, route_id, status='pending', driver_id=None, vehicle_id=None, estimated_delivery=None):
    shipment = Shipment(
        customer_id=customer_id,
        warehouse_id=warehouse_id,
        route_id=route_id,
        status=status,
        driver_id=driver_id,
        vehicle_id=vehicle_id,
        estimated_delivery=estimated_delivery,
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
    if not shipment:
        return None
    for key, value in kwargs.items():
        setattr(shipment, key, value)
    shipment.updated_at = datetime.now()
    session.commit()
    return shipment

def delete_shipment(session, shipment_id):
    shipment = session.query(Shipment).get(shipment_id)
    if not shipment:
        return False
    session.delete(shipment)
    session.commit()
    return True

