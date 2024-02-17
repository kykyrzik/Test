from typing import Annotated, AsyncContextManager

from fastapi import APIRouter, Depends
from redis.asyncio import Redis

from src.service.database.core import get_session, transaction_gateway
from src.common.dto.user import UserCreateDTO, UserInDB
from src.service.database.repr.user import UserRepository
from src.service.redis.connection import connect_redis

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("/")
async def user_create(user: UserCreateDTO,
                      gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))],
                      redis_client: Annotated[Redis, Depends(connect_redis)]
                      ) -> dict[str, UserInDB]:
    user_repr: UserRepository = (await gateway.__aenter__()).user()
    refer_email = await redis_client.get(user.referrer)
    result = await user_repr._create(user.model_copy(update={"referrer": refer_email}))
    return {'result': result}
