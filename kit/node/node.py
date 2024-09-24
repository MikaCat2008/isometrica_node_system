from __future__ import annotations

from typing import TypeVar, Iterable, Generator, TYPE_CHECKING

from ..serialization import Serializable

if TYPE_CHECKING:
    from ..component.component import Component

NodeT = TypeVar("NodeT", bound="Node")


class Node(Serializable):    
    nodes: list[Node]
    components: list[Component]

    parent: Node
    is_alive: bool

    def initialize(self) -> None:
        super().__init__()

        for node in self.nodes:
            node.parent = self

        for component in self.components:
            component.node = self

    def add_nodes(self, *nodes: Node) -> None:
        self.nodes.extend(
            node.update_fields(parent=self) for node in nodes
        )

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
