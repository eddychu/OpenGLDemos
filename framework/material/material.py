from framework.core.uniform import Uniform, UniformDataType
from framework.core.shader import Shader
from OpenGL.GL import *


class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCode) -> None:
        self.shader = Shader(
            vertexShaderCode, fragmentShaderCode)

        self.uniforms = {}

        self.uniforms["modelMatrix"] = Uniform(UniformDataType.MAT4, None)
        self.uniforms["viewMatrix"] = Uniform(UniformDataType.MAT4, None)
        self.uniforms["projectionMatrix"] = Uniform(UniformDataType.MAT4, None)

        self.settings = {}
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, variableName, dataType, data):
        self.uniforms[variableName] = Uniform(dataType, data)

    def updateRenderSettings(self):
        pass

    def setProperties(self, properties):
        for name, data in properties.items():
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            elif name in self.settings.keys():
                self.settings[name] = data
            else:
                raise Exception("Material has no property named: " + name)
