from typing import TypeVar

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

SessionFactory = TypeVar("SessionFactory")


def create_engine(url) -> AsyncEngine:
    return create_async_engine(url, echo=False)


def create_as_session_maker(engine: AsyncEngine) -> SessionFactory:
    return async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)