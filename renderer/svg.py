import xml.etree.cElementTree as ET


class Svg:
    def __init__(
        self,
        width: float,
        height: float,
        attributes: dict[str, str] = {},
        stroke_width: float = 3,
    ):
        self.width = width
        self.height = height

        self.stroke_width = stroke_width

        margin = stroke_width / 2

        self.svg = ET.Element(
            "svg",
            attrib=attributes,
            width=str(width + 2 * margin),
            height=str(height + 2 * margin),
            xmlns="http://www.w3.org/2000/svg",
        )

        self.rect = ET.SubElement(
            self.svg,
            "g",
            width=str(width),
            height=str(height),
            transform=f"translate({margin}, {margin})",
        )
        self.parts = []

    def moveto(self, x: float, y: float):
        self._command("M", x, y)

    def lineto(self, x: float, y: float):
        self._command("L", x, y)

    def closepath(self):
        self.parts.append("Z")

    def _command(self, command: str, x: float, y: float):
        y = self.height - y
        self.parts.append(f"{command}{x} {y}")

    def write(self, path: str):
        d = " ".join(self.parts)
        ET.SubElement(
            self.rect,
            "path",
            d=d,
            style=f"fill:none;stroke:green;stroke-width:{self.stroke_width}",
        )

        tree = ET.ElementTree(self.svg)
        tree.write(path)
