from sqlalchemy.orm import Session
from .models import User

def create_user(db: Session, user_data):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user