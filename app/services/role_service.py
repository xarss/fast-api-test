from typing import List
from sqlalchemy.orm import Session
from app.models.role_models import Role, RoleResponseDto
from fastapi import HTTPException, status

def create_role(db: Session, name: str, description: str) -> RoleResponseDto:
    db_role = Role(
        name=name,
        description=description
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role_by_id(db: Session, role_id: int) -> RoleResponseDto:
    role = db.query(Role).filter(Role.id == role_id).first()
    
    if(not role):
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Could not find role with Id '{role_id}'"
        )
    
    return role

def get_roles(db: Session) -> List[RoleResponseDto]:
    return list(db.query(Role).all())