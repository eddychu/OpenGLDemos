from framework.material.material import Material
from framework.core.uniform import UniformDataType


class BasicMaterial(Material):

    def __init__(self) -> None:
        vertexShaderCode = """
        #version 460
        in vec3 vertexPosition;

        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
     
        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
        }
        """

        fragmentShaderCode = """
        #version 460
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main()
        {
            fragColor = vec4(baseColor, 1.0);
        }
        """

        super().__init__(vertexShaderCode, fragmentShaderCode)
        self.addUniform("baseColor", UniformDataType.VEC3, [1.0, 0.0, 0.0])
