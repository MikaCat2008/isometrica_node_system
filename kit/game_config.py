from __future__ import annotations

from .serialization import serialize_field, Serializable


class GameConfig(Serializable):
    flags: int = serialize_field(int, default=lambda: 0)
    screen_size: tuple[int, int] = serialize_field(tuple[int, int], default=lambda: (0, 0))
