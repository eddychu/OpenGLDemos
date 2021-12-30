from framework.core.attribute import Attribute
from framework.core.object3D import Object3D


class Geometry(Object3D):

    def __init__(self) -> None:
        super().__init__()
        self.attributes = {}
        self.vertexCount = None

    def addAttribute(self, variableName, dataType, data):
        self.attributes[variableName] = Attribute(dataType, data)

    def countVertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
