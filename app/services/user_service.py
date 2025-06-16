from typing                    import List
from sqlalchemy.orm            import Session
from app.models.user_models    import User, UserResponseDto
from fastapi                   import HTTPException, status

from app.services.password_service import hashed

def create_user(db: Session, username: str, email: str, role_id: int = 1) -> UserResponseDto:    
    if db.query(User).filter(User.email == email or User.username == username).first():
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            "Username or email already registered"
        )
    
    db_user = User(
        username = username,
        email = email,
        role_id = role_id
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def get_user_by_id(db: Session, id: int) -> UserResponseDto:
    return db.query(User).filter(User.id == id).first()

def get_users(db: Session) -> List[UserResponseDto]:
    return list(db.query(User).all())

def update_user(db: Session, id: int, username: str, email: str) -> UserResponseDto:
    db_user = db.query(User).filter(User.id == id).first()
    
    if(not db_user):
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Could not find user with Id '{id}'"
        )
    
    db_user.username = username # type: ignore
    db_user.email = email # type: ignore
    
    db.commit()
    db.refresh(db_user)
    
    return db_user

def update_user_password(db: Session, email: str, new_password: str) -> None:
    user = db_user = db.query(User).filter(User.email == email).first()
    user.password = hashed(new_password) # type: ignore
    
    db.commit()
    db.refresh(db_user)

def update_user_google_id(db: Session, email: str, google_id: str) -> None:
    user = db_user = db.query(User).filter(User.email == email).first()
    user.google_id = google_id # type: ignore
    
    db.commit()
    db.refresh(db_user)

def update_user_role(db: Session, id: int, role_id: int) -> UserResponseDto:
    db_user = db.query(User).filter(User.id == id).first()
    
    if(not db_user):
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            f"Could not find user with Id '{id}'"
        )
    
    db_user.role_id = role_id # type: ignore
    
    db.commit()
    db.refresh(db_user)
    
    return db_user