from pygame.surface import Surface

from kit import Node


class SceneNode(Node):
    image: Surface
    position: tuple[int, int]

    def update(self) -> bool:
        super().update()

        return self.is_alive

    def serialize(self) -> dict:
        return {
            "position": self.position
        } | super().serialize()

    def deserialize(self, data: dict) -> None:
        super().deserialize(data)

        position: list[int] = data["position"]

        self.image = Surface((1, 1))
        self.position = tuple(position)
