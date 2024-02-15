from typing import Annotated, AsyncContextManager

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.service.database.core import transaction_gateway, get_session

from src.service.database.repr.user import UserRepository
from src.common.dto.token import Token


login_router = APIRouter(prefix="/login")


@login_router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))]
                                 ):

    user_repr: UserRepository = (await gateway.__aenter__()).user()
    return await user_repr.authenticate(form_data)
