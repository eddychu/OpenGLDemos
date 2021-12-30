from framework.geometry.polygonGeometry import PolygonGeometry


class HexagonGeometry(PolygonGeometry):
    def __init__(self,  radius=1) -> None:
        super().__init__(sides=6, radius=radius)
