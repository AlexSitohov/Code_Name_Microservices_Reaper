from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from httpx import AsyncClient

from JWT import create_access_token, get_current_user
from hash import verify_password

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
    username = current_user.get('username')
    user_id = current_user.get('user_id')
    return {"message": f"Hello {username}. Your id is {user_id}. You have successfully authenticated."}


@app.post("/login")
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
    username = login_data.username
    password = login_data.password
    async with AsyncClient() as client:
        response = await client.get(f"http://31.129.97.191:82/users/username/{username}")
        result = response.json()
    user_id = result.get('id')
    user_username = result.get('username')
    user_password = result.get('password')

    if not username == user_username or not await verify_password(password, user_password):
        raise HTTPException(status_code=400, detail="Неправильный логин или пароль")

    access_token = create_access_token(data={'user_id': user_id,
                                             'username': user_username,
                                             })

    return {"access_token": access_token, "token_type": "bearer"}
