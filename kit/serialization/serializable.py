from abc import ABC, abstractmethod
from typing import Any, TypeVar

SerializableT = TypeVar("SerializableT", bound="Serializable")


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        ...
    
    @abstractmethod
    def initialize(self, data: dict) -> None:
        ...

    @abstractmethod
    def deserialize(self, serialized_data: dict) -> dict:
        ...

    def copy(self: SerializableT) -> SerializableT:
        cls = self.__class__

        return cls(self.serialize())

    def update_fields(self: SerializableT, **fields: Any) -> SerializableT:
        for attr, value in fields.items():
            setattr(self, attr, value)

        return self
