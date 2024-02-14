from typing import AsyncIterable
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession

from .unit_of_work import factory_unit_of_work
from .gateway import database_gateway_factory, DatabaseGateway
from .session import create_as_session_maker, create_engine
from src.core.settings import load_setting


def get_session() -> AsyncSession:
    factory_session = create_as_session_maker(create_engine(load_setting().db_setting.get_url))
    return factory_session()


@asynccontextmanager
async def transaction_gateway(session: AsyncSession) -> AsyncIterable[DatabaseGateway]:
    gateway = database_gateway_factory(factory_unit_of_work(session))
    async with gateway:
        yield gateway