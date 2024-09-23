from __future__ import annotations

import random
import pygame as pg

from kit import GameConfig, GameManager
from scene import Scene
from scenes_manager import ScenesManager
from textures_manager import TexturesManager

from nodes import nodes
from components import components

pg.init()


class Game(GameManager, init=False):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(config)

        TexturesManager()

        self.nodes.register_nodes(nodes)
        self.components.register_components(components)

        main_scene = Scene({
            "root_node": {
                "nodes": [
                    {
                        "nodes": [],
                        "components": [
                            {
                                "__component_name__": "FpsTextComponent"
                            }
                        ],

                        "text": "",
                        "position": [0, 0],

                        "__node_name__": "TextNode"
                    }
                ] + [
                    {
                        "nodes": [],
                        "components": [
                            {
                                "__component_name__": "RandomizedTextComponent"
                            }
                        ],

                        "text": "",
                        "position": (random.randint(0, 512), random.randint(0, 288)),

                        "__node_name__": "TextNode"
                    }
                    for _ in range(3_000)
                ],
                "components": []
            }
        })
        
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
