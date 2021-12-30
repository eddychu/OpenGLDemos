from framework.core.attribute import AttributeDataType
from framework.geometry.geometry import Geometry


class BoxGeometry(Geometry):

    def __init__(self, width=1, height=1, depth=1) -> None:
        super().__init__()
        P0 = [-width/2, -height/2, -depth/2]
        P1 = [width/2, -height/2, -depth/2]
        P2 = [-width/2,  height/2, -depth/2]
        P3 = [width/2,  height/2, -depth/2]
        P4 = [-width/2, -height/2,  depth/2]
        P5 = [width/2, -height/2,  depth/2]
        P6 = [-width/2,  height/2,  depth/2]
        P7 = [width/2,  height/2,  depth/2]

        T0, T1, T2, T3 = [0, 0], [1, 0], [0, 1], [1, 1]

        uvData = [T0, T1, T3, T0, T3, T2] * 6

        positionData = [P5, P1, P3, P5, P3, P7, P0, P4, P6, P0,
                        P6, P2, P6, P7, P3, P6, P3, P2,
                        P0, P1, P5, P0, P5, P4, P4, P5, P7,
                        P4, P7, P6, P1, P0, P2, P1, P2, P3]

        N1, N2 = [1, 0, 0], [-1, 0, 0]
        N3, N4 = [0, 1, 0], [0, -1, 0]
        N5, N6 = [0, 0, 1], [0, 0, -1]
        normalData = [N1] * 6 + [N2] * 6 + [N3] * \
            6 + [N4] * 6 + [N5] * 6 + [N6] * 6

        self.addAttribute("vertexPosition",
                          AttributeDataType.VEC3, positionData)
        # self.addAttribute("vertexNormal", AttributeDataType.VEC3, normalData)
        # self.addAttribute("vertexUV", AttributeDataType.VEC2, uvData)
        self.countVertices()
