from __future__ import annotations
import abc
from typing import Protocol, Generic

from sqlalchemy.ext.asyncio import AsyncSession

from src.common.types import SessionType, TransactionType


class UnitOfWork(Protocol):
    @abc.abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class AbstractUnitOfWork(UnitOfWork, Generic[SessionType, TransactionType]):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self) -> AbstractUnitOfWork[SessionType, TransactionType]:
        await self.create_transaction()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._transaction:
            if exc_type:
                await self.rollback()
            else:
                await self.commit()

        await self.close_transaction()