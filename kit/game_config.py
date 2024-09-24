from __future__ import annotations

from .serialization.serializable import Serializable


class GameConfig(Serializable):
    flags: int   
    screen_size: tuple[int, int]

    def serialize(self) -> dict:
        return {
            "flags": self.flags,
            "screen_size": self.screen_size
        }
    
    def initialize(self, data: dict) -> None:
        super().initialize(data)

        flags: int = data["flags"]
        screen_size: tuple[int, int] = data["screen_size"]

        self.flags = flags
        self.screen_size = screen_size

    def deserialize(self, serialized_data: dict) -> None:
        flags: int = serialized_data["flags"]
        serialized_screen_size: tuple[int, int] = serialized_data["screen_size"]

        screen_size = tuple(serialized_screen_size)

        return {
            "flags": flags,
            "screen_size": screen_size
        }
