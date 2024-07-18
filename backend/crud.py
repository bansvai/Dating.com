import random
from sqlalchemy.orm import Session
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
    return db.query(User).offset(random_index).limit(1).first()