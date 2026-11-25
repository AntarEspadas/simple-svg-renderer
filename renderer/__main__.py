from .svg import Svg
from .mesh import Mesh
import numpy as np


def render(mesh: Mesh, svg: Svg):
    for edge in mesh.edges:
        a, b = mesh.points[list(edge)]
        svg.moveto(a[0], a[1])
        svg.lineto(b[0], b[1])


def main():

    points = [
        (0, 0, 0),
        (0, 100, 0),
        (100, 0, 0),
        (100, 100, 0),
        (0, 0, 100),
        (0, 100, 100),
        (100, 100, 100),
    ]
    # edges = [(0, 1), (0, 2), (1, 3), (2, 3), (0, 4), (1, 5), (4, 5), (3, 6), (5, 6)]
    # mesh = Mesh(np.array(points), edges)

    # mesh.rotate_y(45)
    # mesh.rotate_x(45)

    mesh = Mesh.build_regular_tetrahedron(100)
    mesh.rotate_y(25)
    # mesh.rotate_x(90)

    mesh.translate(150, 10)

    svg = Svg(400, 210, {"stroke-linecap": "round"})

    render(mesh, svg)

    svg.write("output/image.svg")


if __name__ == "__main__":
    main()
