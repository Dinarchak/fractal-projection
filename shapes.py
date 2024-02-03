import typing
from abc import ABC, abstractmethod
from numpy import linalg
import numpy as np
from utils import Vector, normalize

class Shape(ABC):
    @abstractmethod
    def dist(self, point: Vector) -> float:
        pass

class Circle(Shape):
    def __init__(self, center: Vector, radius: float):
        self.center = center
        self.radius = radius

    def dist(self, point: Vector) -> float:
        return (linalg.norm(point - self.center) - self.radius)
