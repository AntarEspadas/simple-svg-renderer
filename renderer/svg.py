import xml.etree.cElementTree as ET


class Svg:
    def __init__(self, width: int, height: int, attributes: dict[str, str]):
        self.width = width
        self.height = height

        self.svg = ET.Element(
            "svg",
            attrib=attributes,
            width=str(width),
            height=str(height),
            xmlns="http://www.w3.org/2000/svg",
        )
        self.parts = []

    def moveto(self, x: int, y: int):
        self._command("M", x, y)

    def lineto(self, x: int, y: int):
        self._command("L", x, y)

    def closepath(self):
        self.parts.append("Z")

    def _command(self, command: str, x: int, y: int):
        y = self.height - y
        self.parts.append(f"{command}{x} {y}")

    def write(self, path: str):
        d = " ".join(self.parts)
        ET.SubElement(
            self.svg,
            "path",
            d=d,
            style="fill:none;stroke:green;stroke-width:3",
        )

        tree = ET.ElementTree(self.svg)
        tree.write(path)
