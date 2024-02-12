from typing import AsyncIterable

from sqlalchemy.ext.asyncio import AsyncSession

from src.service.database.core.unit_of_work import SQLAlchemyUnitOfWork
from src.service.database.repr.user import UserRepository
from src.service.database.core.unit_of_work import factory_unit_of_work


class DatabaseGateway:
    def __init__(self, uow: SQLAlchemyUnitOfWork):
        self.uow = uow

    async def __aenter__(self):
        await self.uow.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.uow.__aexit__(exc_type, exc_val, exc_tb)

    def media(self) -> MediaRepr:
        return UserRepository(self.uow.session)


def database_gateway_factory(unit_of_work: SQLAlchemyUnitOfWork) -> DatabaseGateway:
    return DatabaseGateway(unit_of_work)


async def transaction_gateway(session: AsyncSession) -> AsyncIterable[DatabaseGateway]:
    gateway = database_gateway_factory(factory_unit_of_work(session))
    async with gateway:
        yield gateway