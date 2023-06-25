from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from httpx import AsyncClient
from fastapi.middleware.cors import CORSMiddleware

import schemas
from verify_token import get_current_user

app = FastAPI(title='api_gateway')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api/users/ping")
async def gateway_users_ping(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191/")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/api/users")
async def gateway_get_users_list(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191/users")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.post("/api/users")
async def gateway_create_user(user_data: schemas.UserCreateSchema):
    try:
        async with AsyncClient() as client:
            response = await client.post("http://31.129.97.191/users", json=user_data.dict())
            json_data = response.json()
            return JSONResponse(content=json_data)
    except:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/api/auth/ping")
async def gateway_auth_microservice_ping(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:81/")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.post("/api/auth/login")
async def gateway_auth_login(login_data: OAuth2PasswordRequestForm = Depends()):
    username = login_data.username
    password = login_data.password
    async with AsyncClient() as client:
        response = await client.post("http://31.129.97.191:81/login", data={"username": username, "password": password})
        json_data = response.json()
        return JSONResponse(content=json_data)


@app.get("/api/auth/auth_ping")
async def auth_ping(request: Request, current_user=Depends(get_current_user)):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:81/auth_ping",
                                    headers={'Authorization': request.headers.get('Authorization')})
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)
