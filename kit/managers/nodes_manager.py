from __future__ import annotations

from typing import TYPE_CHECKING

from .manager import Manager

if TYPE_CHECKING:
    from .node import Node


class NodesManager(Manager):
    node_factories: dict[str, type[Node]]
    
    def __init__(self) -> None:
        super().__init__()

        self.node_factories = {}

    def register_nodes(self, nodes: list[type[Node]]) -> None:
        for node in nodes:
            self.node_factories[node.__name__] = node

    def deserialize_node(self, data: dict) -> Node:
        node_name: str = data["__node_name__"]
        factory = self.node_factories[node_name]
        
        return factory(data)
