from app.models import Driver

def create_driver(session, name, phone=None, license_number=None):
    driver = Driver(name=name, phone=phone, license_number=license_number)
    session.add(driver)
    session.commit()
    return driver

def get_drivers(session):
    return session.query(Driver).all()

def update_driver(session, driver_id, **kwargs):
    driver = session.query(Driver).get(driver_id)
    if not driver:
        return None
    for key, value in kwargs.items():
        setattr(driver, key, value)
    session.commit()
    return driver

def delete_driver(session, driver_id):
    driver = session.query(Driver).get(driver_id)
    if not driver:
        return False
    session.delete(driver)
    session.commit()
    return True

