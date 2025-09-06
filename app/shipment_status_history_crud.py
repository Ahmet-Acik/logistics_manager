from app.models import ShipmentStatusHistory
from datetime import datetime

def create_shipment_status_history(session, shipment_id, status):
    history = ShipmentStatusHistory(
        shipment_id=shipment_id,
        status=status,
        timestamp=datetime.now()
    )
    session.add(history)
    session.commit()
    return history

def get_shipment_status_histories(session, shipment_id=None):
    query = session.query(ShipmentStatusHistory)
    if shipment_id:
        query = query.filter_by(shipment_id=shipment_id)
    return query.all()

