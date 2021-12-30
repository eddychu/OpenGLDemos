from framework.geometry.geometry import Geometry
from framework.core.attribute import AttributeDataType


class RectangleGeometry(Geometry):

    def __init__(self, width=1, height=1) -> None:
        super().__init__()
        p0 = [-width/2, -height/2, 0]
        p1 = [width/2, -height/2, 0]
        p2 = [-width/2, height/2, 0]
        p3 = [width/2, height/2, 0]

        c0, c1, c2, c3 = [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]

        t0, t1, t2, t3 = [0, 0], [1, 0], [0, 1], [1, 1]

        normalVector = [0, 0, 1]
        normalData = [normalVector] * 6

        positionData = [p0, p1, p3, p0, p3, p2]
        colorData = [c0, c1, c3, c0, c3, c2]
        uvData = [t0, t1, t3, t0, t3, t2]
        self.addAttribute("vertexPosition",
                          AttributeDataType.VEC3, positionData)
        self.addAttribute("vertexNormal", AttributeDataType.VEC3, normalData)
        self.addAttribute("vertexUV", AttributeDataType.VEC2, uvData)
        self.countVertices()
