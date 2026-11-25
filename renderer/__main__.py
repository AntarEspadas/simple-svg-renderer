from .svg import Svg
import numpy as np
import pyvista as pv


def render(mesh: pv.DataSet):
    bounds = mesh.bounds

    mesh = mesh.translate((-bounds.x_min, -bounds.y_min, 0))

    width = mesh.bounds.x_max
    height = mesh.bounds.y_max

    edges = mesh.extract_all_edges()

    V = np.asarray(edges.points)
    E = np.asarray(edges.lines).reshape(-1, 3)[:, 1:]

    svg = Svg(width, height, {"stroke-linecap": "round"})
    for edge in E:
        a, b = V[list(edge)]
        svg.moveto(a[0], a[1])
        svg.lineto(b[0], b[1])

    return svg


def main():

    mesh = pv.read("models/d10.obj")

    assert isinstance(mesh, pv.DataSet)

    svg = render(mesh)

    svg.write("output/image.svg")


if __name__ == "__main__":
    main()
