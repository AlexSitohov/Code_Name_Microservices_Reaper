from fastapi import APIRouter, Request, HTTPException
from httpx import AsyncClient
from fastapi.responses import JSONResponse

import schemas

router = APIRouter(tags=['users'])


@router.get("/api/users/ping")
async def gateway_users_ping(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:82/")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.get("/api/users")
async def gateway_get_users_list(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:82/users")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.post("/api/users")
async def gateway_create_user(user_data: schemas.UserCreateSchema):
    try:
        async with AsyncClient() as client:
            response = await client.post("http://31.129.97.191:82/users", json=user_data.dict())
            json_data = response.json()
            return JSONResponse(content=json_data)
    except:
        raise HTTPException(status_code=500, detail="Internal server error")