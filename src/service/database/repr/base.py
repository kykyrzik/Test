from typing import Type, Optional, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (select,
                        update,
                        delete)
from sqlalchemy.exc import NoResultFound

from src.common.db.base import AbstractCRUDRepository
from src.common.types import Model, SessionType


class SQLAlchemyRepository(AbstractCRUDRepository[SessionType, Model]):
    model: Type[Model]

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def create(self, data: dict) -> Optional[Model]:
        new_obj = self.model(**data)
        self._session.add(new_obj)
        await self._session.commit()
        await self._session.refresh(new_obj)
        return new_obj

    async def read(self, field: Any, value: Any) -> Optional[Model]:
        try:
            stmt = (select(self.model)
                    .where(value == field)
                    )
            result = await self._session.scalar(stmt)
            return result
        except NoResultFound:
            return None

    async def update(self, field: Any, value: Any, data: dict) -> Optional[Model]:
        stmt = (update(self.model)
                .where(field == value)
                .values(**data)
                .returning(self.model)
                )
        result = await self._session.scalar(stmt)
        await self._session.commit()
        await self._session.refresh(result)
        return result

    async def delete(self, field: Any, model_id: Any) -> bool:
        stmt = (
            delete(self.model).
            where(field == model_id)
        )
        result = await self._session.execute(stmt)
        await self._session.commit()
        if result.rowcount:
            return True
        return False
