from pydantic import BaseModel

class GoogleUser(BaseModel):
    id: str
    email: str
    username: str

class AccessTokenResponse(BaseModel):
    access_token: str

class LoginDto(BaseModel):
    email: str
    password: str

class GoogleLoginDto(BaseModel):
    id_token: str

class RegisterDto(BaseModel):
    username: str
    email: str
    password: str