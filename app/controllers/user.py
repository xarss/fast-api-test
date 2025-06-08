from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.user import create_user, get_user_by_id, get_users, update_user, update_user_role
from app.models.user import CreateUserDto, UpdateUserRoleDto, UserResponseDto, UpdateUserDto

router = APIRouter()

@router.get("/users/", response_model=list[UserResponseDto])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db=db)

@router.post("/users/", response_model=UserResponseDto)
def create_user_endpoint(dto: CreateUserDto, db: Session = Depends(get_db)):
    return create_user(db=db, dto=dto)

@router.get("/users/{user_id}", response_model=UserResponseDto)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db=db, user_id=user_id)
    if user:
        return user
    return {"error": "User not found"}

@router.put("/users/{id}", response_model=UserResponseDto)
def update_user_endpoint(dto: UpdateUserDto, db: Session = Depends(get_db)):
    return update_user(db=db, dto=dto)

@router.put("/users/{id}/role", response_model=UserResponseDto)
def update_user_role_endpoint(dto: UpdateUserRoleDto, db: Session = Depends(get_db)):
    return update_user_role(db=db, dto=dto)