from sqlalchemy.orm import Session
from app.models.user import  User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.stud_id == user_id).first()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, updated_data : dict):
    user = db.query(User).filter(User.stud_id == user_id).first()
    if user:
        for key,value in updated_data.items():
            setattr(user,key,value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int ):
    user = db.query(User).filter(User.stud_id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
