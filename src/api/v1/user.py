from typing import Annotated

from fastapi import APIRouter, Depends

from src.service.database.core.gateway import DatabaseGateway
from src.service.database.core import get_session, transaction_gateway
from src.common.dto.user import UserCreateDTO, UserInDB
# from src.common.convert.user import convert_user_model_to_dto

user_router = APIRouter()


@user_router.post("/")
async def user_create(user: UserCreateDTO,
                      gateway: Annotated[DatabaseGateway, Depends(lambda: transaction_gateway(get_session()))]
                      ) -> dict[str, UserInDB]:

    result = await gateway.user().create(user)
    return {'result': result}
