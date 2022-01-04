from framework.material.material import Material
from framework.core.uniform import Uniform, UniformDataType


class PBRMaterial(Material):

    def __init__(self) -> None:
        vertexShaderCode = """
        #version 460
        in vec3 vertexPosition;
        in vec3 vertexNormal;
        in vec2 vertexUV;

        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;

        out vec3 position;
        out vec3 normal;
        out mat4 viewMatrix_;

        void main() {
            mat4 modelViewMatrix = viewMatrix * modelMatrix;
            mat4 normalMatrix = transpose(inverse(modelViewMatrix));
            normal = normalize(mat3(normalMatrix) * vertexNormal);
            position = vec3(modelViewMatrix * vec4(vertexPosition, 1.0));
            viewMatrix_ = viewMatrix;
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
        }
        """

        fragmentShaderCode = """
        #version 460
        const float PI = 3.14159265358979323846;
        in vec3 position;
        in vec3 normal;
        in mat4 viewMatrix_;

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

        uniform struct Material {
            float rough;
            bool metal;
            vec3 albedo;
        } material;

        out vec4 FragColor;
        float ggxDistribution(float nDotH) {
            float alpha2 = material.rough * material.rough * material.rough * material.rough;
            float d = (nDotH * nDotH) * (alpha2 - 1.0) + 1.0;
            return alpha2 / (PI * d * d);
        }

        float geomSmith(float dotProd) {
            float k = (material.rough + 1.0) * (material.rough + 1.0) / 8.0;
            float denom = dotProd * (1.0 - k) + k;
            return 1.0 / denom;
        }

        vec3 schlickFresnel(float lDotH) {
            vec3 f0 = vec3(0.04);
            if (material.metal) {
                f0 = material.albedo;
            }
            return f0 + (vec3(1.0) - f0) * pow(1.0 - lDotH, 5.0);
        }

        vec3 microfacetModel(vec3 pos, vec3 n) {
            vec3 diffuseBrdf = vec3(0.0);
            if(!material.metal) {
                diffuseBrdf = material.albedo;    
            }
            vec3 l = vec3(viewMatrix_ * vec4(light0.position, 1.0)) - pos,
                i = light0.color;
            float dist = length(l);
            l = normalize(l);
            i /= (dist * dist);

            vec3 v = normalize(-pos);
            vec3 h = normalize(l + v);
            float nDotH = dot(n,h);
            float lDotH = dot(l,h);
            float nDotL = max(dot(n, l), 0.0);
            float nDotV = dot(n,v);
            vec3 specBrdf = 0.25 * ggxDistribution(nDotH) * schlickFresnel(lDotH) * geomSmith(nDotL) * geomSmith(nDotV);
            return (diffuseBrdf + PI * specBrdf) * i * nDotL;
        }

        void main() {
            vec3 n = normalize(normal);
            FragColor = vec4(microfacetModel(position, n), 1.0);
        }
        """
        super().__init__(vertexShaderCode, fragmentShaderCode)

        self.addUniform("light0", UniformDataType.LIGHT, None)
        self.addUniform("light1", UniformDataType.LIGHT, None)
        self.addUniform("light2", UniformDataType.LIGHT, None)
        self.addUniform("light3", UniformDataType.LIGHT, None)
        self.addUniform("material.albedo",
                        UniformDataType.VEC3, [1.0, 0.71, 0.29])
        self.addUniform("material.rough", UniformDataType.FLOAT, 0.43)
        self.addUniform("material.metal", UniformDataType.BOOL, True)

        self.locateUniforms()
