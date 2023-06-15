from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database_config import get_db
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


@app.get("/users", status_code=status.HTTP_201_CREATED)
async def get_users_list(session: AsyncSession = Depends(get_db)):
    users_list = await session.execute(
        select(models.User))
    return users_list.scalars().all()
