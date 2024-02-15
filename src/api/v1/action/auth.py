from typing import Annotated, AsyncContextManager

from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from src.common.dto.user import UserInDB
from src.service.database.core import transaction_gateway, get_session
from src.service.database.repr.user import UserRepository
from src.service.security import jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def get_current_user_from_token(token: Annotated[oauth2_scheme, Depends()],
                                      gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))]
                                      ) -> UserInDB:

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"},
                                          )
    payload = jwt.decode_access_token(token)
    if payload is None:
        raise credentials_exception
    email: str = payload.get("sub")

    user_repr: UserRepository = (await gateway.__aenter__()).user()
    user = await user_repr.get(email)
    if not user:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserInDB, Depends(get_current_user_from_token)]
):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
