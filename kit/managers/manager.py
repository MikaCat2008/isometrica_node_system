from __future__ import annotations

from typing import Type, TypeVar, ClassVar

ManagerT = TypeVar("ManagerT", bound="Manager")


class Manager:
    instance: Manager
    instances: ClassVar[dict[str, Manager]] = {}

    def __init_subclass__(cls, init: bool = True) -> None:
        if init:
            cls()

    def __init__(self) -> None:
        cls = self.__class__
        
        for _cls in cls.__mro__:
            if _cls is not Manager and Manager in _cls.__mro__:
                _cls.set_instance(self)
    
        cls.instances[cls.__name__] = self

    @classmethod
    def set_instance(cls, instance: Manager) -> None:
        cls.instance = instance

    @classmethod
    def get_instance(cls: Type[ManagerT]) -> ManagerT:
        return cls.instance

    @classmethod
    def get_manager(cls, name: str) -> Manager:
        return cls.instances[name]
