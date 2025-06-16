from fastapi import HTTPException, status
import jwt
import datetime
from typing import Any
from ..config import JWT_SECRET_KEY

def create_jwt_token(id: str, email: str, username: str, role_id: int) -> str:
    try:
        payload: dict[str, Any] = {
            "sub": id,
            "email": email,
            "name": username,
            "role_id": role_id,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        }
        
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")
        return token
    except:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Could not generate JSON Web Token"
        )