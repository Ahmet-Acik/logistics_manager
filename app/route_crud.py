from app.models import Route

def create_route(session, origin, destination, distance_km):
    route = Route(origin=origin, destination=destination, distance_km=distance_km)
    session.add(route)
    session.commit()
    return route

def get_routes(session):
    return session.query(Route).all()

def update_route(session, route_id, **kwargs):
    route = session.query(Route).get(route_id)
    if not route:
        return None
    for key, value in kwargs.items():
        setattr(route, key, value)
    session.commit()
    return route

def delete_route(session, route_id):
    route = session.query(Route).get(route_id)
    if not route:
        return False
    session.delete(route)
    session.commit()
    return True
