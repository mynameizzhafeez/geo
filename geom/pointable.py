from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Tuple

class Pointable(ABC):
    x: float
    y: float
    
    @abstractmethod
    def __init__(self, x: float, y: float):
        pass
    
    @abstractmethod
    def get_closest_point(self, *points: Pointable) -> Tuple[Optional[Pointable], float]:
        pass
        