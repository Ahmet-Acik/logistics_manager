
import uuid
from datetime import datetime, timedelta, UTC
import pytest

from app import (
    create_customer, get_customers, update_customer, delete_customer,
    create_warehouse, get_warehouses, update_warehouse, delete_warehouse,
    create_route, get_routes, update_route, delete_route,
    create_driver, get_drivers, update_driver, delete_driver,
    create_vehicle, get_vehicles, update_vehicle, delete_vehicle,
    create_shipment, get_shipments, update_shipment, delete_shipment,
    create_tracking, get_trackings,
    create_shipment_status_history, get_shipment_status_histories,
    create_user, update_user, delete_user, authenticate_user,
    get_shipments_by_warehouse, get_shipments_by_route, get_shipments_by_driver, get_shipments_by_vehicle,
    get_customer_order_history
)
from app.database import SessionLocal


@pytest.fixture(scope="module")
def session():
    s = SessionLocal()
    yield s
    s.close()

# Test cases remain unchanged

def test_customer_crud(session):
    unique_email = f"test_{uuid.uuid4().hex}@example.com"
    c = create_customer(session, "Test Customer", unique_email, "1234567890")
    assert c.id is not None
    customers = get_customers(session)
    assert any(cu.id == c.id for cu in customers)
    updated = update_customer(session, c.id, name="Updated Customer")
    assert updated.name == "Updated Customer"
    assert delete_customer(session, c.id) is True

def test_warehouse_crud(session):
    w = create_warehouse(session, "Test Warehouse", "Test Location")
    assert w.id is not None
    warehouses = get_warehouses(session)
    assert any(wh.id == w.id for wh in warehouses)
    updated = update_warehouse(session, w.id, name="Updated Warehouse")
    assert updated.name == "Updated Warehouse"
    assert delete_warehouse(session, w.id) is True

def test_route_crud(session):
    r = create_route(session, "Origin", "Destination", 100.0)
    assert r.id is not None
    routes = get_routes(session)
    assert any(rt.id == r.id for rt in routes)
    updated = update_route(session, r.id, origin="New Origin")
    assert updated.origin == "New Origin"
    assert delete_route(session, r.id) is True

def test_driver_vehicle_crud(session):
    unique_license = f"LIC{uuid.uuid4().hex[:6]}"
    unique_plate = f"PLATE{uuid.uuid4().hex[:6]}"
    d = create_driver(session, "Driver Name", "555-5555", unique_license)
    v = create_vehicle(session, unique_plate, "Truck", 1000)
    assert d.id is not None and v.id is not None
    drivers = get_drivers(session)
    vehicles = get_vehicles(session)
    assert any(dr.id == d.id for dr in drivers)
    assert any(ve.id == v.id for ve in vehicles)
    assert update_driver(session, d.id, name="New Driver").name == "New Driver"
    assert update_vehicle(session, v.id, type="Van").type == "Van"
    assert delete_driver(session, d.id) is True
    assert delete_vehicle(session, v.id) is True

def test_shipment_crud_and_reporting(session):
    unique_email = f"cust_{uuid.uuid4().hex}@example.com"
    unique_license = f"LIC{uuid.uuid4().hex[:6]}"
    unique_plate = f"PLATE{uuid.uuid4().hex[:6]}"
    c = create_customer(session, "Customer", unique_email)
    w = create_warehouse(session, "Warehouse", "Location")
    r = create_route(session, "Origin", "Destination", 50.0)
    d = create_driver(session, "Driver", "555-1234", unique_license)
    v = create_vehicle(session, unique_plate, "Truck", 2000)
    est_delivery = datetime.now(UTC) + timedelta(days=5)
    s = create_shipment(session, c.id, w.id, r.id, driver_id=d.id, vehicle_id=v.id, estimated_delivery=est_delivery)
    assert s.id is not None
    shipments = get_shipments(session)
    assert any(sh.id == s.id for sh in shipments)
    assert update_shipment(session, s.id, status="in_transit").status == "in_transit"
    assert get_shipments_by_warehouse(session, w.id)[0].id == s.id
    assert get_shipments_by_route(session, r.id)[0].id == s.id
    assert get_shipments_by_driver(session, d.id)[0].id == s.id
    assert get_shipments_by_vehicle(session, v.id)[0].id == s.id
    assert delete_shipment(session, s.id) is True
    delete_customer(session, c.id)
    delete_warehouse(session, w.id)
    delete_route(session, r.id)
    delete_driver(session, d.id)
    delete_vehicle(session, v.id)

def test_tracking_and_status_history(session):
    unique_email = f"cust2_{uuid.uuid4().hex}@example.com"
    c = create_customer(session, "Customer2", unique_email)
    w = create_warehouse(session, "Warehouse2", "Location2")
    r = create_route(session, "Origin2", "Destination2", 75.0)
    s = create_shipment(session, c.id, w.id, r.id)
    t = create_tracking(session, s.id, "picked_up", "Warehouse2")
    assert t.id is not None
    assert get_trackings(session)[-1].shipment_id == s.id
    h = create_shipment_status_history(session, s.id, "picked_up")
    assert h.id is not None
    assert get_shipment_status_histories(session, s.id)[-1].status == "picked_up"
    delete_shipment(session, s.id)
    delete_customer(session, c.id)
    delete_warehouse(session, w.id)
    delete_route(session, r.id)

def test_user_authentication(session):
    unique_username = f"admin_{uuid.uuid4().hex[:6]}"
    u = create_user(session, unique_username, "password", "admin")
    assert u.id is not None
    assert authenticate_user(session, unique_username, "password") is not None
    assert update_user(session, u.id, role="manager").role == "manager"
    assert delete_user(session, u.id) is True

def test_customer_order_history(session):
    unique_email = f"cust3_{uuid.uuid4().hex}@example.com"
    c = create_customer(session, "Customer3", unique_email)
    w = create_warehouse(session, "Warehouse4", "Location4")
    r = create_route(session, "Origin4", "Destination4", 120.0)
    s1 = create_shipment(session, c.id, w.id, r.id, status="delivered")
    s2 = create_shipment(session, c.id, w.id, r.id, status="pending")
    orders = get_customer_order_history(session, c.id)
    assert len(orders) == 2
    delivered_orders = get_customer_order_history(session, c.id, status="delivered")
    assert len(delivered_orders) == 1
    delete_shipment(session, s1.id)
    delete_shipment(session, s2.id)
    delete_customer(session, c.id)
    delete_warehouse(session, w.id)
    delete_route(session, r.id)

if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main([__file__]))
