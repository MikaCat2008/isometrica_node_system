from __future__ import annotations

from typing import ClassVar, TYPE_CHECKING

from ..serializable import Serializable

if TYPE_CHECKING:
    from .node import Node


class Component(Serializable):   
    node: Node

    component_factories: ClassVar[dict[str, type[Component]]] = {}

    def __init_subclass__(cls) -> None:
        cls.component_factories[cls.__name__] = cls

    def serialize(self) -> dict:
        return {
            "__component_name__": self.__class__.__name__
        }

    def deserialize(self, data: dict) -> None:
        ...
