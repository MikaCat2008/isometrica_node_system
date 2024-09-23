from __future__ import annotations

from .serializable import Serializable


class GameConfig(Serializable):
    flags: int   
    screen_size: tuple[int, int]

    def serialize(self) -> dict:
        return {
            "flags": self.flags,
            "screen_size": self.screen_size
        }

    def deserialize(self, data: dict) -> None:
        flags: int = data["flags"]
        screen_size: tuple[int, int] = data["screen_size"]
        
        self.flags = flags
        self.screen_size = screen_size
