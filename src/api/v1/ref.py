from typing import Annotated

from fastapi import APIRouter, Depends

from .action.auth import get_current_user_from_token
from src.common.dto.user import UserInDB

ref_router = APIRouter(prefix="/ref", tags=["ref"])


@ref_router.get("/ref", response_model=UserInDB)
async def get_ref_code(current_user: Annotated[UserInDB, Depends(get_current_user_from_token)]):
    return current_user

