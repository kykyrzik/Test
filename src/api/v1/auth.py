from typing import Annotated, AsyncContextManager

from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm

from src.service.database.core import transaction_gateway, get_session

from src.common.dto.token import Token
from src.service.database.repr.user import UserRepository


login_router = APIRouter(prefix="/login", tags=["Login"])


@login_router.post("/token")
async def login_for_access_token(response: Response,
                                 form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))]
                                 ) -> dict[str, str]:

    user_repr: UserRepository = (await gateway.__aenter__()).user()
    token: dict = await user_repr.authenticate(form_data)
    response.set_cookie("access_token", value=f"{token['access_token']}")
    return {"status": "success"}

