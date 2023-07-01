from fastapi import APIRouter, Request, Depends, HTTPException, status
from httpx import AsyncClient
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from verify_token import get_current_user

router = APIRouter(tags=['auth'])


@router.get("/api/auth/ping", status_code=status.HTTP_200_OK)
async def gateway_auth_microservice_ping(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:81/")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.post("/api/auth/login")
async def gateway_auth_login(login_data: OAuth2PasswordRequestForm = Depends()):
    username = login_data.username
    password = login_data.password
    async with AsyncClient() as client:
        response = await client.post("http://31.129.97.191:81/login", data={"username": username, "password": password})
        json_data = response.json()
        return JSONResponse(content=json_data)


@router.get("/api/auth/auth_ping", status_code=status.HTTP_200_OK)
async def auth_ping(request: Request, current_user=Depends(get_current_user)):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:81/auth_ping",
                                    headers={'Authorization': request.headers.get('Authorization')})
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)
