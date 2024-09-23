from .managers import (
    Node as Node,
    Manager as Manager,
    Component as Component,
    GameManager as GameManager,
    TicksManager as TicksManager,
    NodesManager as NodesManager,
    EventsManager as EventsManager,
    ComponentsManager as ComponentsManager
)
from .serializable import (
    GameConfig as GameConfig,
    Serializable as Serializable
)


def nround(number: float) -> int:
    inumber = int(number)
    real = number - inumber
    sign = real >= 0
    
    if sign:
        return inumber if real < 0.5 else inumber + 1
    
    return inumber if real > -0.5 else inumber - 1
