from typing import TypeVar, Generic, Protocol

T = TypeVar('T')


class Input(Protocol[T]):
    def read(self) -> T:
        ...


class Output(Protocol[T]):
    def write(self, data: T) -> None:
        ...


class PlainFlow(Input[T], Output[T]):
    def __init__(self):
        self._value: T = None

    def write(self, data: T) -> None:
        self._value = data

    def read(self) -> T:
        return self._value
