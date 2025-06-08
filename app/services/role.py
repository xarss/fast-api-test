from typing import List
from sqlalchemy.orm import Session
from app.models.role import Role, RoleResponseDto, CreateRoleDto

def create_role(db: Session, dto: CreateRoleDto) -> RoleResponseDto:
    db_role = Role(
        name=dto.name,
        description=dto.description
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role_by_id(db: Session, user_id: int) -> RoleResponseDto:
    return db.query(Role).filter(Role.id == user_id).first()

def get_roles(db: Session) -> List[RoleResponseDto]:
    return list(db.query(Role).all())