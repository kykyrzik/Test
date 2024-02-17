from datetime import timedelta
from typing import Type, Optional, List

from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm


from .base import SQLAlchemyRepository
from src.service.database.models.user import User
from src.common.dto.user import UserCreateDTO, UserInDB
from src.service.security.security import get_password_hash, verify_password
from src.common.convert.user import convert_user_model_to_dto
from src.common.dto.token import Token
from src.service.security.jwt import create_access_token


class UserRepository(SQLAlchemyRepository):
    model: Type[User] = User

    async def _create(self, data: UserCreateDTO) -> Optional[UserInDB]:
        new_user = data.__dict__
        password = new_user.pop("password")
        new_user["hashed_password"] = get_password_hash(password)
        result = await self.create(data=new_user)
        return convert_user_model_to_dto(result)

    async def get(self, data: str | int) -> Optional[UserInDB]:
        if isinstance(data, str):
            user = await self.read(field=self.model.email, value=data)
        else:
            user = await self.read(field=self.model.id, value=data)
        if not user:
            return None
        return convert_user_model_to_dto(user)

    async def authenticate(self, form_data: OAuth2PasswordRequestForm) -> Token:
        user = await self.get(form_data.username)
        if not user or not verify_password(form_data.password, user.password):
            raise HTTPException(status_code=404, detail="incorrect email or password")
        access_token_minute = timedelta(minutes=15)
        access_token = create_access_token(
            data={"sub": user.email, "scopes": form_data.scopes},
            expires_delta=access_token_minute,
        )
        return Token(access_token=access_token, token_type="Bearer")

    async def get_referrers(self, email: str) -> Optional[List[UserInDB]]:
        result = await self.get_list(field=self.model.referrer, model_id=email)
        return [convert_user_model_to_dto(item) for item in result]
