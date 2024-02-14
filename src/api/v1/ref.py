from fastapi import APIRouter, Request
from fastapi.exceptions import HTTPException

from src.service.security import jwt

ref_router = APIRouter(prefix="/ref", tags=["ref"])


@ref_router.get("/")
async def get_ref_code(request: Request) -> dict[str, str]:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=403,
                            detail="user inactive",
                            )
    payload = jwt.decode_access_token(token)
    if payload:
        return {payload.get("sub"): "111111"}
    raise HTTPException(status_code=401,
                        detail=f"invalid token error:"
                        )