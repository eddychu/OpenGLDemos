from framework.core.attribute import Attribute, AttributeDataType
from OpenGL.GL import *


class InstancedAttribute(Attribute):
    def __init__(self, dataType: AttributeDataType, data, meshPerInstance=1):
        super().__init__(dataType, data)
        self.meshPerInstance = meshPerInstance

    def bindTo(self, location):
        super().bindTo(location)
        glVertexAttribDivisor(location, self.meshPerInstance)

    def update(self):
        super().update()
