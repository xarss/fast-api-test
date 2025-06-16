from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.role_service import create_role, get_role_by_id, get_roles
from app.models.role_models import CreateRoleDto, RoleResponseDto

router = APIRouter(prefix="/roles", tags=["Roles"])


@router.get("/", response_model=list[RoleResponseDto])
def get_roles_endpoint(db: Session = Depends(get_db)):
    return get_roles(db=db)


@router.post("/", response_model=RoleResponseDto)
def create_role_endpoint(dto: CreateRoleDto, db: Session = Depends(get_db)):
    return create_role(db=db, name=dto.name, description=dto.description)


@router.get("/{role_id}", response_model=RoleResponseDto)
def get_role_endpoint(role_id: int, db: Session = Depends(get_db)):
    return get_role_by_id(db=db, role_id=role_id)
