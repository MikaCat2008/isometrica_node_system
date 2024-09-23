from __future__ import annotations

import math
from typing import TYPE_CHECKING

import pygame as pg

from kit import Component, GameManager

if TYPE_CHECKING:
    from nodes import TextNode


class FpsTextComponent(Component):
    node: TextNode

    game: GameManager

    def set_fps(self) -> None:
        fps = self.game.fps

        if math.isfinite(fps):
            fps = int(fps)

        self.node.set_text(f"{fps} fps")

    def deserialize(self, data: dict) -> None:
        super().deserialize(data)

        self.game = GameManager.get_instance()
        self.game.ticks.register(5, self.set_fps)
