from typing import Type

from .base import SQLAlchemyRepository
from src.service.database.models.user import User
from src.common.dto.user import UserCreateDTO, UserInDB
from src.service.database.security import security
from src.common.convert.user import convert_user_model_to_dto


class UserRepository(SQLAlchemyRepository):
    model: Type[User] = User

    async def _create(self, data: UserCreateDTO) -> UserInDB:
        new_user = data.__dict__
        password = new_user.pop("password")
        new_user["hashed_password"] = security.get_password_hash(password)
        result = await self.create(data=new_user)
        return convert_user_model_to_dto(result)