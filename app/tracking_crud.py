from app.models import Tracking
from datetime import datetime

def create_tracking(session, shipment_id, status, location):
    tracking = Tracking(
        shipment_id=shipment_id,
        status=status,
        location=location,
        timestamp=datetime.now()
    )
    session.add(tracking)
    session.commit()
    return tracking

def get_trackings(session):
    return session.query(Tracking).all()

def update_tracking(session, tracking_id, **kwargs):
    tracking = session.query(Tracking).get(tracking_id)
    if not tracking:
        return None
    for key, value in kwargs.items():
        setattr(tracking, key, value)
    session.commit()
    return tracking

def delete_tracking(session, tracking_id):
    tracking = session.query(Tracking).get(tracking_id)
    if not tracking:
        return False
    session.delete(tracking)
    session.commit()
    return True

