from framework.core.attribute import Attribute, AttributeDataType
from framework.core.indexAttribute import IndexAttribute
from framework.core.object3D import Object3D
from framework.extras.objLoader import ObjData, ObjLoader


class Geometry(Object3D):

    @staticmethod
    def loadFromFile(fileName):
        objData = ObjLoader.loadFromFile(fileName)
        geometry = Geometry()

        geometry.addAttribute(
            "vertexPosition", AttributeDataType.VEC3, objData.vertices)
        geometry.addAttribute(
            "vertexNormal", AttributeDataType.VEC3, objData.normals)
        geometry.addAttribute(
            "vertexUV", AttributeDataType.VEC2, objData.texCoords)
        geometry.setIndexAttribute(objData.indices)
        geometry.vertexCount = len(objData.indices)
        return geometry

    def __init__(self) -> None:
        super().__init__()
        self.attributes = {}
        self.vertexCount = None
        self.index = None

    def addAttribute(self, variableName, dataType, data):
        self.attributes[variableName] = Attribute(dataType, data)

    def setIndexAttribute(self, data):
        self.index = IndexAttribute(data)

    def countVertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)
