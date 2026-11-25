from .svg import Svg
import numpy as np
import pyvista as pv
import fire
import os


def render(mesh: pv.DataSet, width: float = 100, height: float = 100, color="#e6e6e6"):
    bounds = mesh.bounds

    actual_width = bounds.x_max - bounds.x_min
    actual_height = bounds.y_max - bounds.y_min

    scale = min(width / actual_width, height / actual_height)

    mesh = mesh.scale(scale)

    bounds = mesh.bounds

    x_translation = (width - bounds.x_min - bounds.x_max) / 2
    y_translation = (height - bounds.y_min - bounds.y_max) / 2

    mesh = mesh.translate((x_translation, y_translation, 0))

    edges = mesh.extract_all_edges()

    V = np.asarray(edges.points)
    E = np.asarray(edges.lines).reshape(-1, 3)[:, 1:]

    svg = Svg(width, height, {"stroke-linecap": "round"}, stroke_color=color)
    for edge in E:
        a, b = V[list(edge)]
        svg.moveto(a[0], a[1])
        svg.lineto(b[0], b[1])

    return svg


def main(*obj_paths: str, out_dir: str | None = None):

    assert len(obj_paths) >= 1, "Provide at least one .obj path"

    for path in obj_paths:
        mesh = pv.read(path)

        assert isinstance(mesh, pv.DataSet)

        svg = render(mesh)

        out_path = os.path.splitext(path)[0] + ".svg"

        if out_dir is not None:
            base_name = os.path.basename(out_path)
            out_path = os.path.join(out_dir, base_name)

        svg.write(out_path)


if __name__ == "__main__":
    fire.Fire(main)
