
from OpenGL.GL import *


class Shader(object):

    def __init__(self, vertexStr: str, fragmentStr: str) -> None:
        super().__init__()
        print(vertexStr)
        print(fragmentStr)
        vertexShader = self.createShader(vertexStr, GL_VERTEX_SHADER)
        fragmentShader = self.createShader(fragmentStr, GL_FRAGMENT_SHADER)
        self.program = glCreateProgram()
        glAttachShader(self.program, vertexShader)
        glAttachShader(self.program, fragmentShader)
        glLinkProgram(self.program)
        if glGetProgramiv(self.program, GL_LINK_STATUS) != GL_TRUE:
            raise Exception(glGetProgramInfoLog(self.program))

        print("attributes: ", glGetProgramiv(
            self.program, GL_ACTIVE_ATTRIBUTES))

        glDeleteShader(vertexShader)
        glDeleteShader(fragmentShader)

    def createShader(self, shaderStr: str, shaderType: int) -> int:
        shader = glCreateShader(shaderType)
        glShaderSource(shader, shaderStr)
        glCompileShader(shader)
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(glGetShaderInfoLog(shader))
        return shader

    def findAttributeLocation(self, name: str) -> int:
        return glGetAttribLocation(self.program, name)

    def findUniformLocation(self, name: str) -> int:
        return glGetUniformLocation(self.program, name)

    def use(self):
        glUseProgram(self.program)

    def destroy(self):
        glDeleteProgram(self.program)
