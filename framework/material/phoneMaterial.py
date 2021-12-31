from framework.material.material import Material
from framework.core.uniform import Uniform, UniformDataType


class PhongMaterial(Material):

    def __init__(self, texture=None, normalTexture=None, properties={}) -> None:
        vertexShaderCode = """
        #version 460
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        in vec3 vertexNormal;
        out vec3 position;
        out vec2 UV;
        out vec3 normal;

        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
            UV = vertexUV;
            position = vec3(modelMatrix * vec4(vertexPosition, 1.0));
            normal = normalize(mat3(modelMatrix) * vertexNormal);
        }

        """

        fragmentShaderCode = """
        #version 460
        struct Light
        {
            int lightType;
            vec3 color;
            vec3 direction;
            vec3 position;
        };

        uniform Light light0;
        uniform Light light1;
        uniform Light light2;
        uniform Light light3;

        uniform vec3 viewPosition;
        uniform float specularStrength;
        uniform float shininess;



        vec3 lightCalc(Light light, vec3 pointPosition, vec3 pointNormal)
        {
            float ambient = 0;
            float diffuse = 0;
            float specular = 0;
            float attenuation = 1;
            vec3 lightDirection = vec3(0, 0, 0);

            if (light.lightType == 1) 
            {
                ambient = 1;
            } else if (light.lightType == 2)
            {
                lightDirection = normalize(light.direction);
            } else if (light.lightType == 3)
            {
                lightDirection = normalize(pointPosition - light.position);
                float distance = length(light.position - pointPosition);
                attenuation = 1.0 / (distance * distance);
            }

            if (light.lightType > 1) 
            {

                pointNormal = normalize(pointNormal);
                diffuse = max(dot(pointNormal, -lightDirection), 0.0);
                diffuse *= attenuation;
                if (diffuse > 0)
                {
                    vec3 viewDirection = normalize(viewPosition - pointPosition);
                    vec3 reflectDirection = reflect(lightDirection, pointNormal);
                    specular = pow(max(dot(viewDirection, reflectDirection), 0.0), shininess);
                    specular = specularStrength * pow(specular, shininess);
                }
            }

            return light.color * (ambient + diffuse + specular);
        }
        uniform bool useTexture;
        uniform sampler2D texture;
        uniform bool useNormalTexture;
        uniform sampler2D normalTexture;

        in vec3 position;
        in vec2 UV;
        in vec3 normal;

        out vec4 fragColor;
        void main() 
        {
            vec4 color = vec4(1.0, 0.0, 0.0, 1.0);
            if (useTexture)
            {
                color = texture2D(texture, UV);
            }
            vec3 bNormal = normal;
            if (useNormalTexture)
            {
                bNormal += normalize(vec3(texture2D(normalTexture, UV)) * 2.0 - 1.0);
            }

            vec3 total = vec3(0, 0, 0);
            total += lightCalc(light0, position, bNormal);
            total += lightCalc(light1, position, bNormal);
            total += lightCalc(light2, position, bNormal);
            total += lightCalc(light3, position, bNormal);
            fragColor = color * vec4(total, 1.0);
        }
        """

        # vec3 total = vec3(0, 0, 0);

        # total += lightCalc(light0, position, normal);
        # total += lightCalc(light1, position, normal);
        # total += lightCalc(light2, position, normal);
        # total += lightCalc(light3, position, normal);

        # color *= vec4(total, 1.0);
        super().__init__(vertexShaderCode, fragmentShaderCode)
        if texture is None:
            self.addUniform("useTexture", UniformDataType.BOOL, False)
        else:
            self.addUniform("useTexture", UniformDataType.BOOL, True)
            self.addUniform(
                "texture", UniformDataType.SAMPLER2D, texture.handle)

        self.addUniform("light0", UniformDataType.LIGHT, None)
        self.addUniform("light1", UniformDataType.LIGHT, None)
        self.addUniform("light2", UniformDataType.LIGHT, None)
        self.addUniform("light3", UniformDataType.LIGHT, None)
        self.addUniform("specularStrength", UniformDataType.FLOAT, 1.0)
        self.addUniform("shininess", UniformDataType.FLOAT, 32.0)
        self.addUniform("viewPosition", UniformDataType.VEC3, [0, 0, 0])

        if normalTexture is None:
            self.addUniform("useNormalTexture", UniformDataType.BOOL, False)
        else:
            self.addUniform("useNormalTexture", UniformDataType.BOOL, True)
            self.addUniform("normalTexture",
                            UniformDataType.SAMPLER2D, normalTexture.handle)

        self.locateUniforms()
