from __future__ import annotations

from typing import TYPE_CHECKING

from pygame.surface import Surface

from kit import Node

if TYPE_CHECKING:
    from kit.scene.scene import Scene


class SceneNode(Node):
    scene: Scene
    image: Surface
    position: tuple[int, int]

    def initialize(self) -> None:
        self.image = Surface((1, 1))

    def update(self) -> bool:
        super().update()

        return self.is_alive

    def serialize(self) -> dict:
        return {
            "position": self.position
        } | super().serialize()

    def initialize(self, data: dict) -> None:
        super().initialize(data)

        position: tuple[int, int] = data["position"]

        self.position = tuple(position)

    def deserialize(self, serialized_data: dict) -> dict:
        serialized_position: list[int] = serialized_data["position"]

        position = tuple(serialized_position)

        return {
            "position": position
        } | super().deserialize(serialized_data)
