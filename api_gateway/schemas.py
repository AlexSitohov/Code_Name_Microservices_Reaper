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


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
