from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models.auth_models import AccessTokenResponse, GoogleLoginDto, LoginDto, RegisterDto
from app.services.auth_service import get_access_token, get_google_access_token, register_user

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login/google", response_model=AccessTokenResponse)
def login_google_user_endpoint(dto: GoogleLoginDto, db: Session = Depends(get_db)) -> AccessTokenResponse:
    return get_google_access_token(db=db, id_token=dto.id_token)

@router.post("/login/password", response_model=AccessTokenResponse)
def login_user_endpoint(dto: LoginDto, db: Session = Depends(get_db)) -> AccessTokenResponse:
    return get_access_token(db=db, email=dto.email, password=dto.password)

@router.post("/register", response_model=AccessTokenResponse)
def register_user_endpoint(dto: RegisterDto, db: Session = Depends(get_db)) -> AccessTokenResponse:
    return register_user(db=db, email=dto.email, username=dto.username, password=dto.password)