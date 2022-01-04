from framework.material.material import Material
from framework.core.uniform import UniformDataType


class BasicMaterial(Material):

    def __init__(self, instanced: bool = False) -> None:
        vertexShaderCode = """
        #version 460
        in vec3 vertexPosition;
        in vec3 instancePosition;

        uniform bool isInstanced;
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
     
        void main()
        {
            vec3 position = vertexPosition;
            if (isInstanced) {
                position = instancePosition + vertexPosition;
            }
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
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
        self.addUniform("isInstanced", UniformDataType.BOOL, instanced)
        self.locateUniforms()
