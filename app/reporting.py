from app.models import Shipment, Inventory

def get_shipments_by_warehouse(session, warehouse_id):
    return session.query(Shipment).filter_by(warehouse_id=warehouse_id).all()

def get_shipments_by_route(session, route_id):
    return session.query(Shipment).filter_by(route_id=route_id).all()

def get_shipments_by_driver(session, driver_id):
    return session.query(Shipment).filter_by(driver_id=driver_id).all()

def get_shipments_by_vehicle(session, vehicle_id):
    return session.query(Shipment).filter_by(vehicle_id=vehicle_id).all()

def get_customer_order_history(session, customer_id, status=None, start_date=None, end_date=None):
    query = session.query(Shipment).filter_by(customer_id=customer_id)
    if status:
        query = query.filter_by(status=status)
    if start_date:
        query = query.filter(Shipment.created_at >= start_date)
    if end_date:
        query = query.filter(Shipment.created_at <= end_date)
    return query.all()

def get_low_stock_alerts(session, threshold=10):
    low_stock = session.query(Inventory).filter(Inventory.quantity < threshold).all()
    alerts = []
    for inv in low_stock:
        alerts.append({
            'warehouse_id': inv.warehouse_id,
            'item_name': inv.item_name,
            'quantity': inv.quantity
        })
    return alerts

