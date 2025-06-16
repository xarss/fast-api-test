from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base
from pydantic import BaseModel


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    description = Column(String(500), index=True)

    # Relationships
    users = relationship("User", back_populates="role")


class CreateRoleDto(BaseModel):
    name: str
    description: str


class RoleResponseDto(CreateRoleDto):
    id: int

    class Config:
        from_attributes = True
