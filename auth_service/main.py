from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from auth_service.JWT import create_access_token, get_current_user

app = FastAPI(title='auth')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def ping():
    return {"message": "Hello World. This is auth microservice."}


@app.get("/auth_ping")
async def auth_ping(current_user=Depends(get_current_user)):
    return {"message": "Hello. You have successfully authenticated."}


@app.post("/login")
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
    # Проверка правильности введенных данных пользователя
    if not login_data.username == "myuser" and login_data.password == "mypassword":
        raise HTTPException(status_code=400, detail="Неправильный логин или пароль")
    access_token = create_access_token(data={'user_id': '123',
                                             'username': login_data.username,
                                             })

    return {"access_token": access_token, "token_type": "bearer"}
