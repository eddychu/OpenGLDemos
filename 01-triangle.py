from framework.core.base import Base
from framework.core.shader import Shader
from framework.core.vertexarray import VertexArray
from framework.core.matrix import Matrix
from framework.core.attribute import AttributeDataType, Attribute
from framework.core.uniform import UniformDataType, Uniform
from OpenGL.GL import *


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "01-a-triangle"

    def initialize(self):
        print("Initializing {}...".format(self.name))

        vsCode = """
        #version 460
        in vec3 position;
        uniform mat4 modelMatrix;
        uniform mat4 projectionMatrix;
        void main()
        {
            gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
        }
        """

        fsCode = """
        #version 460
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.shader = Shader(vsCode, fsCode)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        self.vao = VertexArray()
        self.vao.bind()
        positionData = [[0.0, 0.2, 0.0], [0.1, -0.2, 0.0], [-0.1, -0.2, 0.0]]
        self.vertexCount = len(positionData)
        self.positionAttribute = Attribute(
            AttributeDataType.VEC3, positionData)
        self.positionAttribute.bindTo(
            self.shader.findAttributeLocation("position"))
        self.vao.unbind()
        mMatrix = Matrix.makeTranslation(0, 0, -1)
        self.modelMatrix = Uniform(UniformDataType.MAT4, mMatrix)
        self.modelMatrix.locateVariable(self.shader.program, "modelMatrix")
        pMatrix = Matrix.makePerspective()
        self.projectionMatrix = Uniform(UniformDataType.MAT4, pMatrix)
        self.projectionMatrix.locateVariable(
            self.shader.program, "projectionMatrix")

    def update(self):
        glClear(GL_COLOR_BUFFER_BIT)
        self.shader.use()
        self.vao.bind()
        self.modelMatrix.upload()
        self.projectionMatrix.upload()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


if __name__ == "__main__":
    Example().run()
