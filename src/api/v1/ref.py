from typing import Annotated, Final
from secrets import token_urlsafe

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from redis.asyncio import Redis
from email_validator import validate_email, EmailSyntaxError

from .action.auth import get_current_user_from_token
from src.common.dto.user import UserInDB
from src.service.redis.connection import connect_redis

TIMEOUT: Final[int] = 500

ref_router = APIRouter(prefix="/ref", tags=["ref"])


@ref_router.get("/ref")
async def get_ref_code(email: str,
                       current_user: Annotated[UserInDB, Depends(get_current_user_from_token)],
                       redis_client: Annotated[Redis, Depends(connect_redis)]
                       ) -> str:
    try:
        validate_email(email)
    except EmailSyntaxError as e:
        raise HTTPException(status_code=401, detail=e)

    if email != current_user.email:
        raise HTTPException(status_code=401, detail="email is not auth")

    ref_code = token_urlsafe(8)
    old_ref_code = await redis_client.get(email)
    if old_ref_code:
        await redis_client.delete(old_ref_code)
    await redis_client.set(ref_code, email, ex=TIMEOUT)
    await redis_client.set(email, ref_code, ex=TIMEOUT)

    return ref_code


@ref_router.delete("/delete_ref")
async def delete_ref_code(email: str,
                          current_user: Annotated[UserInDB, Depends(get_current_user_from_token)],
                          redis_client: Annotated[Redis, Depends(connect_redis)]
                          ) -> dict[str, str]:
    try:
        validate_email(email)
    except EmailSyntaxError as e:
        raise HTTPException(status_code=401, detail=e)

    if email != current_user.email:
        raise HTTPException(status_code=401, detail="email is not auth")

    old_ref_code = await redis_client.get(email)
    await redis_client.delete(old_ref_code)
    await redis_client.delete(email)
    return {"message": "success"}
