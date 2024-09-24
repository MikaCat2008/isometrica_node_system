from __future__ import annotations

import random
from typing import TYPE_CHECKING

from kit import Component, GameManager

if TYPE_CHECKING:
    from nodes import TextNode


class RandomizedTextComponent(Component):
    node: TextNode

    game: GameManager

    def set_text(self) -> None:
        self.node.set_text(str(random.randint(100_000, 999_999)))

    def initialize(self, data: dict) -> None:
        self.game = GameManager.get_instance()
        self.game.ticks.register(1, self.set_text)

    def deserialize(self, serialized_data: dict) -> dict:
        return {}
