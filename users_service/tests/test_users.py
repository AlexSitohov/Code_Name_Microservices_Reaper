import pytest
from sqlalchemy import insert, select
from fastapi import status

from .conftest import client, async_session_maker


async def test_get_empty_users_list():
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []


async def test_create_user():
    response = client.post("/users", json={

        "username": "test_username",
        "first_name": "test_first_name",
        "last_name": "test_last_name",
        "password": "test_password",
        "email": "test_email@gmail.com",
        "phone": "test_phone_89898988989",
        "city": "test_city_NY"
    }
                           )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().get('username') == 'test_username'
    assert response.json().get('first_name') == 'test_first_name'
    assert response.json().get('last_name') == 'test_last_name'
    assert response.json().get('email') == 'test_email@gmail.com'
    assert response.json().get('phone') == 'test_phone_89898988989'
    assert response.json().get('city') == 'test_city_NY'


async def test_get_users_list():
    response = client.get("/users")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0].get('username') == 'test_username'
    assert response.json()[0].get('first_name') == 'test_first_name'
    assert response.json()[0].get('last_name') == 'test_last_name'
    assert response.json()[0].get('email') == 'test_email@gmail.com'
    assert response.json()[0].get('phone') == 'test_phone_89898988989'
    assert response.json()[0].get('city') == 'test_city_NY'


async def test_get_user_by_username():
    username = 'test_username'
    response = client.get(f"/users/username/{username}")
    assert response.json().get('username') == 'test_username'
    assert response.json().get('first_name') == 'test_first_name'
    assert response.json().get('last_name') == 'test_last_name'
    assert response.json().get('email') == 'test_email@gmail.com'
    assert response.json().get('phone') == 'test_phone_89898988989'
    assert response.json().get('city') == 'test_city_NY'


async def test_get_user_by_username_false():
    username = 'false_test_username'
    response = client.get(f"/users/username/{username}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
