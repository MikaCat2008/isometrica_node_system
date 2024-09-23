from abc import ABC, abstractmethod


class Serializable(ABC):
    def __init__(self, serialized_data: dict) -> None:
        self.deserialize(serialized_data)

    @abstractmethod
    def serialize(self) -> dict:
        ...
    
    @abstractmethod
    def deserialize(self, data: dict) -> None:
        ...
