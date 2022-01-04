from framework.core.attribute import AttributeDataType
from framework.core.mesh import Mesh
from framework.geometry.geometry import Geometry
from framework.material.lineMaterial import LineMaterial


class AxesHelper(Mesh):
    def __init__(self, length=1, lineWidth=4):
        geo = Geometry()
        positionData = [[0, 0, 0], [length, 0, 0],
                        [0, 0, 0], [0, length, 0],
                        [0, 0, 0], [0, 0, length]]

        geo.addAttribute("vertexPosition",
                         AttributeDataType.VEC3, positionData)
        geo.countVertices()

        material = LineMaterial()

        super().__init__(geo, material)
