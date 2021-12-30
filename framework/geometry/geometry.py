from framework.core.attribute import AttributeDataType, Attribute
from framework.core.object3D import Object3D


class Geometry(Object3D):

    def __init__(self) -> None:
        super().__init__()
        self.attributes = {}
        self.vertexCount = 0

    def addAttribute(self, name, dataType, data):
        self.attributes[name] = Attribute(dataType, data)

    def countVertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
