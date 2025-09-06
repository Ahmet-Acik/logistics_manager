from app.models import User

def create_user(session, username, password, role):
    user = User(username=username, password=password, role=role)
    session.add(user)
    session.commit()
    return user

def get_users(session):
    return session.query(User).all()

def update_user(session, user_id, **kwargs):
    user = session.query(User).get(user_id)
    if not user:
        return None
    for key, value in kwargs.items():
        setattr(user, key, value)
    session.commit()
    return user

def delete_user(session, user_id):
    user = session.query(User).get(user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True

def authenticate_user(session, username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    return user

