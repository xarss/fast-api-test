from google.oauth2 import id_token
from google.auth.transport import requests
from passlib.context import CryptContext
from app.models.auth_models import AccessTokenResponse, GoogleUser
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.user_models import User
from app.services.jwt_service import create_jwt_token
from app.services.password_service import verify_password
from app.services.user_service import create_user, update_user_google_id, update_user_password
from ..config import GOOGLE_CLIENT_ID

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_google_token(id_token_str: str) -> GoogleUser:
    id_info: dict[str, str] = id_token.verify_oauth2_token(id_token_str, requests.Request(), GOOGLE_CLIENT_ID) # type: ignore
    
    google_id: str | None = id_info.get("sub")
    email: str | None = id_info.get("email")
    name: str | None = id_info.get("name")
    
    if(not google_id or not email or not name):
        raise ValueError("Could not fetch Google OAuth Token")
    
    return GoogleUser(
        id = google_id,
        email = email,
        username = name
    )

def get_google_access_token(db: Session, id_token: str) -> AccessTokenResponse:
    google_user = verify_google_token(id_token)
    user = db.query(User).filter(User.google_id == google_user.id).first()

    if not user:
        user = create_user(db, username=google_user.username, email=google_user.email)
        update_user_google_id(db, email=google_user.username, google_id=google_user.id)

    jwt_token = create_jwt_token(
        id=user.id, # type: ignore
        email=user.email, # type: ignore
        username=user.username, # type: ignore
        role_id=user.role_id # type: ignore
    )

    return AccessTokenResponse(access_token=jwt_token)

# This method REQUIRES that the user exists
def get_access_token(db: Session, email: str, password: str) -> AccessTokenResponse:
    user = db.query(User).filter(User.email == email).first()

    if not user or not user.password or not verify_password(password, user.password): # type: ignore
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Invalid email or password"
        )

    token = create_jwt_token(
        id=user.google_id or str(user.id), # fallback if not Google user # type: ignore
        email=user.email, # type: ignore
        username=user.username, # type: ignore
        role_id=user.role_id # type: ignore
    )

    return AccessTokenResponse(access_token=token)

def register_user(db: Session, username: str, email: str, password: str) -> AccessTokenResponse:
    create_user(db, username=username, email=email)
    update_user_password(db, email, password)

    return get_access_token(db=db, email=email, password=password)