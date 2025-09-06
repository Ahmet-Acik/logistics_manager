from app.models import Vehicle

def create_vehicle(session, plate_number, type=None, capacity=None):
    vehicle = Vehicle(plate_number=plate_number, type=type, capacity=capacity)
    session.add(vehicle)
    session.commit()
    return vehicle

def get_vehicles(session):
    return session.query(Vehicle).all()

def update_vehicle(session, vehicle_id, **kwargs):
    vehicle = session.query(Vehicle).get(vehicle_id)
    if not vehicle:
        return None
    for key, value in kwargs.items():
        setattr(vehicle, key, value)
    session.commit()
    return vehicle

def delete_vehicle(session, vehicle_id):
    vehicle = session.query(Vehicle).get(vehicle_id)
    if not vehicle:
        return False
    session.delete(vehicle)
    session.commit()
    return True

