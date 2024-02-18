from typing import Annotated, AsyncContextManager, Optional, List

from fastapi import APIRouter, Depends, HTTPException
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
    if user.referrer is not None:
        refer_email = await redis_client.get(user.referrer)
        if not refer_email:
            raise HTTPException(status_code=401, detail="code is not found")
    result = await user_repr._create(user.model_copy(update={"referrer": refer_email}))
    return {'result': result}


@user_router.get("/get_referrers")
async def get_referrers(user_id: int,
                        gateway: Annotated[AsyncContextManager, Depends(lambda: transaction_gateway(get_session()))]
                        ) -> Optional[List[UserInDB]]:
    user_repr: UserRepository = (await gateway.__aenter__()).user()
    user_referrer_email = await user_repr.get(user_id)
    if user_referrer_email:
        raise HTTPException(status_code=404, detail="incorrect user id")
    return await user_repr.get_referrers(user_referrer_email)
