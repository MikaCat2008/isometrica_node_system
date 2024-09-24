from __future__ import annotations

import pickle
from typing import Any, Type, TypeVar, ClassVar

ManagerT = TypeVar("ManagerT", bound="Manager")
SerializableT = TypeVar("SerializableT", bound="Serializable")


class Manager:
    instance: Manager

    def __init_subclass__(cls, init: bool = True) -> None:
        if init:
            cls()

    def __init__(self) -> None:        
        for cls in self.__class__.__mro__:
            if cls is not Manager and Manager in cls.__mro__:
                cls.set_instance(self)

    @classmethod
    def set_instance(cls, instance: Manager) -> None:
        cls.instance = instance

    @classmethod
    def get_instance(cls: Type[ManagerT]) -> ManagerT:
        return cls.instance


class Serializable:
    serializable_fields: ClassVar[list[str]]

    def __init_subclass__(cls) -> None:
        cls.serializable_fields = [
            key for key, value in cls.__dict__.items()
            if isinstance(value, SerializableField)
        ]

    def __getstate__(self) -> dict:
        return {
            key: self.__dict__[key]
            for key in self.__class__.serializable_fields
        }
    
    def __setstate__(self, state: dict) -> None:
        for key in self.__class__.serializable_fields:
            setattr(self, key, state[key])


class SerializableField:
    ...


class SerializationManager(Manager):
    def __init__(self) -> None:
        super().__init__()

    def serialize(self, serializable: Serializable) -> bytes:
        return pickle.dumps(serializable)

    def deserialize(self, serialized_data: bytes) -> Serializable:
        return pickle.loads(serialized_data)


sm = SerializationManager()


class Node(Serializable):
    nodes: list[Node] = SerializableField()
    components: list[Component] = SerializableField()


class Component(Serializable):
    node: Node


node = Node()
node.nodes = []
node.components = []

serialized_data = sm.serialize(node)

node_r = sm.deserialize(serialized_data)

print(node_r)
