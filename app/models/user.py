from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from pydantic import BaseModel
from app.models.role import Role, RoleResponseDto

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
 
    # Relationships
    role = relationship(Role, back_populates="users")

class CreateUserDto(BaseModel):
    username: str
    email: str
    role_id: int

class UserResponseDto(CreateUserDto):
    id: int
    role: RoleResponseDto

    class Config:
        from_attributes = True