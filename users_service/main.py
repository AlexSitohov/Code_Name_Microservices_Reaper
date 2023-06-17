from uuid import UUID

from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database_config import get_db
from schemas import UserSchema, UserCreateSchema
from hash import hash_password

import models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def ping():
    return {"message": "Hello World"}


@app.get("/users", status_code=status.HTTP_200_OK, response_model=list[UserSchema])
async def get_users_list(session: AsyncSession = Depends(get_db)):
    users_list = await session.execute(
        select(models.User))
    return users_list.scalars().all()


@app.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=UserSchema)
async def get_user(user_id: UUID, session: AsyncSession = Depends(get_db)):
    user = await session.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateSchema, session: AsyncSession = Depends(get_db)):
    user_data.password = await hash_password(user_data.password)
    new_user = models.User(**user_data.dict())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: UUID, user_data: UserCreateSchema, session: AsyncSession = Depends(get_db)):
    user = await session.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_data.password = await hash_password(user_data.password)
    user_data_dict = user_data.dict(exclude_unset=True)
    for field, value in user_data_dict.items():
        setattr(user, field, value)

    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: UUID, session: AsyncSession = Depends(get_db)):
    user = await session.get(models.User, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    await session.delete(user)
    await session.commit()
    return "deleted"
