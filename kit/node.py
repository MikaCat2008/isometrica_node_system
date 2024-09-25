from __future__ import annotations

from typing import TypeVar, Optional, Generator, TYPE_CHECKING

from .serialization import serialize_field, Serializable

if TYPE_CHECKING:
    from .scene import Scene
    from .component import Component

NodeT = TypeVar("NodeT", bound="Node")


class Node(Serializable):
    _nodes: list[Node] = serialize_field(list, lambda: [], "nodes")
    _components: list[Component] = serialize_field(list, lambda: [], "components")

    scene: Scene
    parent: Optional[Node] = None
    is_alive: bool

    def __init__(self) -> None:
        super().__init__()

        self.is_alive = True

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

    @property
    def nodes(self) -> list[Node]:
        return self._nodes
    
    @nodes.setter
    def nodes(self, value: list[Node]) -> None:
        self._nodes = value

        for node in self.nodes:
            node.parent = self

    @property
    def components(self) -> list[Component]:
        return self._components
    
    @components.setter
    def components(self, value: list[Component]) -> None:
        self._components = value

        for component in self.components:
            component.node = self
