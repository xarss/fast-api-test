from typing import List
from sqlalchemy.orm import Session
from app.models.user import User, UserResponseDto, CreateUserDto, UpdateUserDto, UpdateUserRoleDto
from fastapi import HTTPException

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

def update_user(db: Session, dto: UpdateUserDto) -> UserResponseDto | HTTPException:
    db_user = db.query(User).filter(User.id == dto.id).first()
    
    if(not db_user):
        return HTTPException(404, f"Could not find user with Id '{dto.id}'")
    
    db_user.username = dto.username # type: ignore
    db_user.email = dto.email # type: ignore
    
    db.commit()
    db.refresh(db_user)
    
    return db_user

def update_user_role(db: Session, dto: UpdateUserRoleDto) -> UserResponseDto | HTTPException:
    db_user = db.query(User).filter(User.id == dto.id).first()
    
    if(not db_user):
        return HTTPException(404, f"Could not find user with Id '{dto.id}'")
    
    db_user.role_id = dto.role_id # type: ignore
    
    db.commit()
    db.refresh(db_user)
    
    return db_user