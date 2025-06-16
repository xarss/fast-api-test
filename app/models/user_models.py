from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from pydantic import BaseModel
from app.models.role_models import Role, RoleResponseDto


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    google_id = Column(String(255), index=True, nullable=True)
    password = Column(String(255), index=True, nullable=True)

    # Relationships
    role = relationship(Role, back_populates="users")


class CreateUserDto(BaseModel):
    username: str
    email: str
    role_id: int


class UserResponseDto(BaseModel):
    id: int
    username: str
    email: str
    google_id: str | None
    role: RoleResponseDto

    class Config:
        from_attributes = True


class UpdateUserDto(BaseModel):
    username: str
    email: str


class UpdateUserRoleDto(BaseModel):
    role_id: int
