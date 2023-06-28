from pydantic import BaseModel, EmailStr
from uuid import UUID


class UserSchema(BaseModel):
    id: UUID
    username: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    phone: str
    city: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr
    phone: str
    city: str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class VerifyEmailCode(BaseModel):
    verification_token: str
