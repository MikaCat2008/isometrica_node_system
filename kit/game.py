from __future__ import annotations

import time

from pygame.time import Clock
from pygame.event import get as get_events
from pygame.surface import Surface
from pygame.display import flip, set_mode

from .serialization import GameConfig

from .node.node import Node
from .manager import Manager
from .builtin_managers.ticks_manager import TicksManager
from .node.node_manager import NodesManager
from .builtin_managers.events_manager import EventsManager
from .component.component_manager import ComponentsManager


class GameManager(Manager, init=False):
    fps: float
    clock: Clock
    ticks: TicksManager
    nodes: NodesManager
    events: EventsManager
    components: ComponentsManager

    screen: Surface

    _draw_interval: float
    _update_interval: float

    def __init__(self, config: GameConfig) -> None:
        super().__init__()

        self.fps = 0
        self.clock = Clock()
        self.ticks = TicksManager()
        self.nodes = NodesManager()
        self.events = EventsManager()
        self.components = ComponentsManager()

        self.nodes.register_nodes([Node])

        self.screen = set_mode(
            size=config.screen_size, 
            flags=config.flags
        )

        self._draw_interval = 1 / 2400
        self._update_interval = 1 / 60

    def update(self) -> None:
        self.ticks.update()

    def draw(self) -> None:
        flip()

    def run(self) -> None:
        last_draw_time = 0
        last_update_time = 0

        while 1:
            current_time = time.time()

            for event in get_events():
                self.events.broadcast(event)

            if current_time - last_update_time > self._update_interval:
                self.update()

                last_update_time = current_time

            if current_time - last_draw_time > self._draw_interval:
                self.draw()

                last_draw_time = current_time

            self.fps = self.clock.get_fps()
            self.clock.tick(2400)
