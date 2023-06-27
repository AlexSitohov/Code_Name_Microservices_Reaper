from datetime import datetime

from pydantic import BaseModel
from uuid import UUID


class UserSchema(BaseModel):
    id: UUID
    username: str
    first_name: str
    last_name: str
    password: str
    email: str
    phone: str
    city: str
    email_confirmed: bool
    email_confirmed_date_time: datetime

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: str
    phone: str
    city: str

    class Config:
        orm_mode = True


class VerifyEmailCode(BaseModel):
    verification_token: str
