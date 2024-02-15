from typing import Annotated, AsyncContextManager

from fastapi import APIRouter, Depends

from src.service.database.core import get_session, transaction_gateway
from src.common.dto.user import UserCreateDTO, UserInDB
from src.service.database.repr.user import UserRepository


user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("/")
async def user_create(user: UserCreateDTO,
                      gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))]
                      ) -> dict[str, UserInDB]:
    user_repr: UserRepository = (await gateway.__aenter__()).user()
    result = await user_repr._create(user)
    return {'result': result}
