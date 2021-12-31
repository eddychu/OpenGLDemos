from OpenGL.GL import *
from enum import Enum


class UniformDataType(Enum):
    FLOAT = 1
    INT = 2
    VEC2 = 3
    VEC3 = 4
    VEC4 = 5
    MAT2 = 6
    MAT3 = 7
    MAT4 = 8
    SAMPLER2D = 9


class Uniform(object):

    def __init__(self, dataType: UniformDataType, data) -> None:
        self.dataType = dataType
        self.data = data

    def bind(self, location):
        if self.dataType == UniformDataType.MAT4:
            glUniformMatrix4fv(location, 1, GL_TRUE, self.data)
        elif self.dataType == UniformDataType.VEC4:
            glUniform4f(
                location, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == UniformDataType.VEC3:
            glUniform3f(
                location, self.data[0], self.data[1], self.data[2])
        elif self.dataType == UniformDataType.VEC2:
            glUniform2f(
                location, self.data[0], self.data[1])
        elif self.dataType == UniformDataType.INT:
            glUniform1i(location, self.data)
        elif self.dataType == UniformDataType.FLOAT:
            glUniform1f(location, self.data)
        elif self.dataType == UniformDataType.SAMPLER2D:
            glActiveTexture(GL_TEXTURE0 + self.data)
            glBindTexture(GL_TEXTURE_2D, self.data)
            # glUniform1i(location, self.data)
        else:
            raise Exception("Uniform location + " +
                            str(location) + " has Unknown data type")
