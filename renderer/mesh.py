import numpy as np
from numpy.typing import NDArray
import math


class Mesh:

    @staticmethod
    def build_regular_tetrahedron(l: float):
        triangle_height = math.tan(math.radians(60)) * (l / 2)
        h = math.sqrt(triangle_height**2 - (l / 2) ** 2)

        points = np.array(
            [
                [0, 0, 0],
                [l, 0, 0],
                [l / 2, 0, triangle_height],
                [l / 2, h, triangle_height / 3],
            ]
        )

        edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

        return Mesh(points, edges)

    def __init__(self, points: np.ndarray, edges: list[tuple[int, int]]) -> None:
        self.points: NDArray[np.float64] = points.astype(float)
        self.edges = edges

    def translate(self, x: float, y: float, z: float = 0):
        self.points += np.array([x, y, z])

    def rotate_x(self, degrees: float):
        angle = math.radians(degrees)
        matrix = np.array(
            [
                [1, 0, 0],
                [0, math.cos(angle), -math.sin(angle)],
                [0, math.sin(angle), math.cos(angle)],
            ]
        )

        self.points @= matrix

    def rotate_y(self, degrees: float):
        angle = math.radians(degrees)
        matrix = np.array(
            [
                [math.cos(angle), 0, math.sin(angle)],
                [0, 1, 0],
                [-math.sin(angle), 0, math.cos(angle)],
            ]
        )

        self.points @= matrix

    def rotate_z(self, degrees: float):
        angle = math.radians(degrees)
        matrix = np.array(
            [
                [math.cos(angle), math.sin(angle), 0],
                [-math.sin(angle), math.cos(angle), 0],
                [0, 0, 1],
            ]
        )

        self.points @= matrix

    def bounding_box_2d(self):
        x = self.points[1,]
        y = self.points[:, 1]
        return np.array([[x.min(), y.min()], [x.max(), y.max()]])
