import typing
from camera import Camera
import numpy as np
from utils import Vector, normalize
from shapes import Circle

WIDTH = 11
HEIGHT = 7

def ray_marching(ray, shapes, point, steps=10):
    start_point = point
    for i in range(steps):
        a = min(shape.dist(point) for shape in shapes) 
        if a < 1e-9:
            return np.linalg.norm(point - start_point)
        point = point + ray * a
    return None

def range_into_range(v: float, range1: tuple[float, float], range2: tuple[float, float]) -> float:
    """
        Функция загоняет число из одного отрезка в другой,
        сохраняя при этом соотношение сторон

        v - значение в исходном отрезке
        range1 - исходный отрезок
        range2 - отрезок, в который нужно загнать число
    """
    if range1[0] == v:
        return range2[0]
    l = (range1[1] - v) / (v - range1[0])
    return (range2[1] + l * range2[0]) / (l + 1)


def square_to_square(point: Vector) -> tuple[float, float]:
    """
    Функция загоняет точку из прямоугольника экрана в прямоугольник (-w/h, 1), (w/h, 1), (w/h, -1), (-w/h, -1)

    point - точка на экране
    """
    global WIDTH
    global HEIGHT
    return range_into_range(point[0], (0.0, float(WIDTH) - 1), (- WIDTH / HEIGHT, WIDTH / HEIGHT)), range_into_range(point[1], (0.0, float(HEIGHT) - 1), (1.0, -1.0))


def from_camera_to_world(camera: Camera, point: Vector):
    return camera.pos + np.matmul(point, camera.rotation_matrix_transposed())

camera = Camera(np.array([1.0, 0.0, 0.0]), vertical_view_angle=np.pi/6)
circle = Circle(np.array([1.1, 0.0, 0.4]), 1)

#проверка на то, что СК камеры - правая ДПСК
# print(camera.xAxis, np.linalg.norm(camera.xAxis))  # модуль должен быть равен 1
# print(camera.yAxis, np.linalg.norm(camera.yAxis))  # модуль должен быть равен 1
# print(camera.zAxis, np.linalg.norm(camera.zAxis))  # модуль должен быть равен 1
# print(np.dot(np.cross(camera.xAxis, camera.yAxis), camera.zAxis))  # смешанное произведение равно 1

frame = np.zeros(shape=(HEIGHT, WIDTH))

x = 1 / np.tan(camera.vert_angle)

for h in range(0, HEIGHT):
    for w in range(0, WIDTH):
        y, z = square_to_square(np.array([w, h]))
        ray = normalize(np.array([x, y, z]))
        world_ray = from_camera_to_world(camera, ray) - camera.pos
        dist = ray_marching(world_ray, [circle], camera.pos)
        if dist is not None:
            frame[h][w] = 1

for i in frame:
    for j in i:
        print(j, end=' ')
    print()