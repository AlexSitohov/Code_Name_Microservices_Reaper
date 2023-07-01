from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from api_gateway_config import *

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = ACCESS_TOKEN_EXPIRE_MINUTES

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", scheme_name="JWT")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login", scheme_name="JWT")


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: id = payload.get('user_id')
        username: str = payload.get('username')

        if user_id is None:
            raise credentials_exception
        token_data = {'user_id': user_id, 'username': username}
        return token_data
    except JWTError:
        raise credentials_exception


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(data, credentials_exception)
