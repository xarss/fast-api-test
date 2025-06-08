from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.role import create_role, get_role_by_id, get_roles
from app.models.role import CreateRoleDto, RoleResponseDto

router = APIRouter()

@router.get("/roles/", response_model=list[RoleResponseDto], tags=["Role"])
def get_roles_endpoint(db: Session = Depends(get_db)):
    return get_roles(db=db)

@router.post("/roles/", response_model=RoleResponseDto, tags=["Role"])
def create_role_endpoint(dto: CreateRoleDto, db: Session = Depends(get_db)):
    return create_role(db=db, dto=dto)

@router.get("/roles/{user_id}", response_model=RoleResponseDto, tags=["Role"])
def get_role_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_role_by_id(db=db, user_id=user_id)
    if user:
        return user
    return {"error": "User not found"}