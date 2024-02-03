import typing
import numpy as np
from numpy import linalg

Vector = np.ndarray[float]

def normalize(vec: Vector):
    return vec / linalg.norm(vec)