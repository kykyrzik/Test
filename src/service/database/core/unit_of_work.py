from sqlalchemy.ext.asyncio import AsyncSession, AsyncSessionTransaction

from src.common.db.unit_of_work import AbstractUnitOfWork


class SQLAlchemyUnitOfWork(AbstractUnitOfWork[AsyncSession, AsyncSessionTransaction]):

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def create_transaction(self) -> None:
        if not self.session.in_transaction() and self.session.is_active:
            self._transaction = await self.session.begin()

    async def close_transaction(self) -> None:
        if self.session.is_active:
            await self.session.close()


def factory_unit_of_work(session: AsyncSession) -> SQLAlchemyUnitOfWork:
    return SQLAlchemyUnitOfWork(session)
