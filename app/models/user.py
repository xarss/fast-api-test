from sqlalchemy import Column, Integer, String
from app.db import Base
from pydantic import BaseModel

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    email = Column(String(255), unique=True, index=True)
    

class UserCreate(BaseModel):
    username: str
    email: str

class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True