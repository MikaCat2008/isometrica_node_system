
from __future__ import annotations

import random
import pygame as pg

from kit import Node, GameConfig, GameManager
from kit.scene.scene import Scene
from kit.scene.scene_manager import ScenesManager
from textures_manager import TexturesManager

# from nodes import nodes, TextNode
# from components import components, FpsTextComponent, RandomizedTextComponent

pg.init()


class Game(GameManager, init=False):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(config)

        TexturesManager()

        self.nodes.

        self.scenes = ScenesManager()
        self.scenes.add_scene("main-scene", main_scene)
        self.scenes.set_current("main-scene")

    def draw(self) -> None:
        self.scenes.draw()

        super().draw()


if __name__ == "__main__":
    game = Game(
        config=GameConfig({
            "flags": pg.SCALED | pg.DOUBLEBUF | pg.FULLSCREEN,
            "screen_size": (512, 288)
        })
    )

    game.run()
