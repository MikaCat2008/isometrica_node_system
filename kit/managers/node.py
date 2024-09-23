from __future__ import annotations

from typing import Any, TypeVar, Iterable, Generator, TYPE_CHECKING

from ..serializable import Serializable
from .nodes_manager import NodesManager
from .components_manager import ComponentsManager

if TYPE_CHECKING:
    from .component import Component

NodeT = TypeVar("NodeT", bound="Node")


class Node(Serializable):    
    nodes: list[Node]
    components: list[Component]

    parent: Node
    is_alive: bool

    def __init__(self, serialized_data: dict) -> None:
        super().__init__(serialized_data)

        self.is_alive = True
        self.initialize()

    def initialize(self) -> None:
        for node in self.nodes:
            node.parent = self

        for component in self.components:
            component.node = self

    def set_parent(self, parent: Node) -> Node:
        self.parent = parent
        
        return self

    def add_node(self, node: Node) -> None:
        node.parent = self
        self.nodes.append(node)

    def add_nodes(self, nodes: Iterable[Node]) -> None:
        self.nodes.extend(node.set_parent(self) for node in nodes)

    def remove_node(self, node: Node) -> None:
        node.parent = None
        self.nodes.remove(node)

    def get_nodes(self) -> Generator[Node]:
        yield self
        
        for node in self.nodes:
            yield from node.get_nodes()

    def update(self) -> bool:
        self.nodes = [
            node
            for node in self.nodes
            if node.update()
        ]

        return self.is_alive

    def copy(self: NodeT) -> NodeT:
        cls = self.__class__

        return cls(self.serialize())

    def update_fields(self: NodeT, **fields: Any) -> NodeT:
        for attr, value in fields.items():
            setattr(self, attr, value)

        return self

    def serialize(self) -> dict:
        return {
            "nodes": [
                node.serialize()
                for node in self.nodes
            ],
            "components": [
                component.serialize()
                for component in self.components
            ],
            "__node_name__": self.__class__.__name__
        }

    def deserialize(self, data: dict) -> None:
        nodes: list[dict] = data["nodes"]
        components: list[dict] = data["components"]

        nodes_manager = NodesManager.get_instance()
        components_manager = ComponentsManager.get_instance()

        self.nodes = list(map(nodes_manager.deserialize_node, nodes))
        self.components = list(map(components_manager.deserialize_component, components))
