from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.user_service import (
    create_user,
    get_user_by_id,
    get_users,
    update_user,
    update_user_role,
)
from app.models.user_models import (
    CreateUserDto,
    UpdateUserRoleDto,
    UserResponseDto,
    UpdateUserDto,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserResponseDto])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db=db)


@router.post("/", response_model=UserResponseDto)
def create_user_endpoint(dto: CreateUserDto, db: Session = Depends(get_db)):
    return create_user(
        db=db, username=dto.username, email=dto.email, role_id=dto.role_id
    )


@router.get("/{id}", response_model=UserResponseDto)
def get_user_endpoint(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, id=id)
    if user:
        return user
    return {"error": "User not found"}


@router.put("/{id}", response_model=UserResponseDto)
def update_user_endpoint(id: int, dto: UpdateUserDto, db: Session = Depends(get_db)):
    return update_user(db=db, id=id, email=dto.email, username=dto.username)


@router.put("/{id}/role", response_model=UserResponseDto)
def update_user_role_endpoint(
    id: int, dto: UpdateUserRoleDto, db: Session = Depends(get_db)
):
    return update_user_role(db=db, id=id, role_id=dto.role_id)
