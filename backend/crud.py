import random
from sqlalchemy.orm import Session
from geopy.distance import geodesic
from .models import User

def create_user(db: Session, user_data):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_random_user(db: Session):
    user_count = db.query(User).count()
    if user_count == 0:
        return None
    random_index = random.randint(0, user_count - 1)
    return db.query(User).offset(random_index).first()

def get_nearest_users(db: Session, random_user_latitude: float, random_user_longitude: float, random_user_id: int):
    all_other_users = db.query(User).filter(User.uid != random_user_id).all()
    random_user_location = (random_user_latitude, random_user_longitude)
    nearest_users = sorted(all_other_users, key=lambda user: geodesic(random_user_location, (user.latitude, user.longitude)).meters)[:100]
    return [{"first_name": user.first_name, "last_name": user.last_name, "email": user.email, "latitude": user.latitude, "longitude": user.longitude} for user in nearest_users]