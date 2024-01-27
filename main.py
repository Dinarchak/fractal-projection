import typing
from camera import Camera
import numpy as np

Vector = np.ndarray[float]
WIDTH = 200
HEIGHT = 150

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
    return range_into_range(point[0], (0.0, float(WIDTH)), (- WIDTH / HEIGHT, WIDTH / HEIGHT)), range_into_range(point[1], (0.0, float(HEIGHT)), (1.0, -1.0))

    

a = Camera(np.array([23.0, 11.0, 78.0]))

# проверка на то, что СК камеры - правая ДПСК
# print(a.xAxis, np.linalg.norm(a.xAxis))  # модуль должен быть равен 1
# print(a.yAxis, np.linalg.norm(a.yAxis))  # модуль должен быть равен 1
# print(a.zAxis, np.linalg.norm(a.zAxis))  # модуль должен быть равен 1
# print(np.dot(np.cross(a.xAxis, a.yAxis), a.zAxis))  # смешанное произведение равно 1

frame = np.zeros(shape=(HEIGHT, WIDTH))


