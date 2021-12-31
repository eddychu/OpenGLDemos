from framework.material.material import Material
from OpenGL.GL import *
from framework.core.uniform import UniformDataType, Uniform


class TextureMaterial(Material):

    def __init__(self, texture, properties={}) -> None:
        vertexShaderCode = """
        #version 460
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;

        out vec2 uv;
        void main() {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
            uv = vertexUV;
        }
        """

        fragmentShaderCode = """
        #version 460

        uniform sampler2D texture;
        in vec2 uv;
        out vec4 fragColor;

        void main() {
            fragColor = texture2D(texture, uv);
        }
        
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)

        self.addUniform("texture", UniformDataType.SAMPLER2D, texture.handle)

        # self.settings["doubleSide"] = True
        # self.settings["wireframe"] = False
        # self.settings["lineWidth"] = 1
        # self.setProperties(properties)
