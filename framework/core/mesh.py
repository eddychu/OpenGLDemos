from framework.core.object3D import Object3D
from OpenGL.GL import *
from framework.core.vertexarray import VertexArray


class Mesh(Object3D):
    def __init__(self, geometry, material) -> None:
        super().__init__()
        self.geometry = geometry
        self.material = material
        self.visible = True
        self.vao = VertexArray()
        self.vao.bind()
        if self.geometry.index is not None:
            self.geometry.index.bind()
        for variableName, attributeObject in geometry.attributes.items():
            location = self.material.shader.findAttributeLocation(variableName)
            if location != -1:
                attributeObject.bindTo(location)
        glBindVertexArray(0)
