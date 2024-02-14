import abc
import typing

from src.common.types import Model, SessionType


class AbstractCRUDRepository(abc.ABC,
                             typing.Generic[SessionType, Model]):

    model: typing.Type[Model]

    def __init__(self, session: SessionType) -> None:
        self._session = session

    @abc.abstractmethod
    async def create(self, **values: typing.Any) -> typing.Any:
        raise NotImplementedError

    @abc.abstractmethod
    async def read(self, *clauses: typing.Any) -> typing.Any:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self,
                     *clauses: typing.Any,
                     **values: typing.Any
                     ) -> typing.Any:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *clauses: typing.Any) -> typing.Any:
        raise NotImplementedError
