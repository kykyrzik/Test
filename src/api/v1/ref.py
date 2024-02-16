from typing import Annotated, Final
from secrets import token_urlsafe

from fastapi import APIRouter, Depends
from redis.asyncio import Redis

from .action.auth import get_current_user_from_token
from src.common.dto.user import UserInDB
from src.service.redis.connection import connect_redis

TIMEOUT: Final[int] = 500

ref_router = APIRouter(prefix="/ref", tags=["ref"])


@ref_router.get("/ref")
async def get_ref_code(current_user: Annotated[UserInDB, Depends(get_current_user_from_token)],
                       redis_client: Annotated[Redis, Depends(connect_redis)]):
    ref_code = token_urlsafe(8)
    await redis_client.set(ref_code, current_user.email, ex=TIMEOUT)
    return ref_code


