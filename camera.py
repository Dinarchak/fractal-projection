import typing
import numpy as np
from numpy import linalg
from utils import Vector, normalize



class Camera:
    def __init__(self, look_point: Vector, position: Vector=np.array([0.0, 0.0, 0.0]), vertical_view_angle=np.pi/4.0):
        self.pos = position  # позиция камеры
        self.vert_angle = vertical_view_angle  # угол вертикального обзора в радианах
        self.xAxis = normalize(look_point - self.pos)
        self.yAxis = normalize(np.cross(np.array([0.0, 0.0, 1.0]), self.xAxis))
        self.zAxis = normalize(np.cross(self.xAxis, self.yAxis))

    def rotation_matrix_transposed(self):
        return np.array([self.xAxis, self.yAxis, self.zAxis])

