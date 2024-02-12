from typing import Type

from .base import SQLAlchemyRepository
from src.service.database.models.user import User


class UserRepository(SQLAlchemyRepository):
    model: Type[User] = User
