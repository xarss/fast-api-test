from typing import List
from sqlalchemy.orm import Session
from app.models.user import User, UserResponseDto, CreateUserDto

def create_user(db: Session, dto: CreateUserDto) -> UserResponseDto:
    db_user = User(
        username=dto.username,
        email=dto.email,
        role_id=dto.role_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int) -> UserResponseDto:
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session) -> List[UserResponseDto]:
    return list(db.query(User).all())