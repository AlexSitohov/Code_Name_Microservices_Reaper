from fastapi import APIRouter, Request, HTTPException, Depends, status
from httpx import AsyncClient
from fastapi.responses import JSONResponse
from uuid import UUID
import schemas
from verify_token import get_current_user

router = APIRouter(tags=['users'])


@router.get("/api/users/ping", status_code=status.HTTP_200_OK)
async def gateway_users_ping(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:82/")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.get("/api/users", status_code=status.HTTP_200_OK)
async def gateway_get_users_list(request: Request):
    async with AsyncClient() as client:
        response = await client.get("http://31.129.97.191:82/users")
        if response.status_code == 200:
            return response.json()
        raise HTTPException(status_code=response.status_code, detail=response.text)


@router.post("/api/users", status_code=status.HTTP_201_CREATED)
async def gateway_create_user(user_data: schemas.UserCreateSchema):
    try:
        async with AsyncClient() as client:
            response = await client.post("http://31.129.97.191:82/users", json=user_data.dict())
            json_data = response.json()
            return JSONResponse(content=json_data)
    except:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/api/users/{user_id}", status_code=status.HTTP_200_OK)
async def gateway_update_user(user_id: UUID, user_data: schemas.UserCreateSchema):
    try:
        async with AsyncClient() as client:
            response = await client.put(f"http://31.129.97.191:82/users/{user_id}", json=user_data.dict())
            json_data = response.json()
            return JSONResponse(content=json_data)
    except:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/api/verify-email", status_code=status.HTTP_200_OK)
async def gateway_verify_email(data: schemas.VerifyEmailCode, request: Request, current_user=Depends(get_current_user)):
    try:
        async with AsyncClient() as client:
            response = await client.put("http://31.129.97.191:82/verify-email", json=data.dict(),
                                        headers={'Authorization': request.headers.get('Authorization')})
            json_data = response.json()
            return JSONResponse(content=json_data)
    except:
        raise HTTPException(status_code=500, detail="Internal server error")
