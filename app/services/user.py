from sqlalchemy.orm import Session
from app.models.user import User, UserResponse

def create_user(db: Session, username: str, email: str) -> UserResponse:
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> UserResponse:
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session) -> list[UserResponse]:
    return list(db.query(User).all())