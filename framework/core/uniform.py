from OpenGL.GL import *
from enum import Enum
from framework.light.light import Light


class UniformDataType(Enum):
    BOOL = 0
    FLOAT = 1
    INT = 2
    VEC2 = 3
    VEC3 = 4
    VEC4 = 5
    MAT2 = 6
    MAT3 = 7
    MAT4 = 8
    SAMPLER2D = 9
    LIGHT = 10


class Uniform(object):

    def __init__(self, dataType: UniformDataType, data) -> None:
        self.dataType = dataType
        self.data = data
        self.variableRef = None

    def locateVariable(self, programRef, variableName):
        if self.dataType == UniformDataType.LIGHT:
            print(variableName)
            self.variableRef = {}
            self.variableRef["lightType"] = glGetUniformLocation(
                programRef, variableName + ".lightType")
            self.variableRef["color"] = glGetUniformLocation(
                programRef, variableName + ".color")

            self.variableRef["position"] = glGetUniformLocation(
                programRef, variableName + ".position")
            self.variableRef["direction"] = glGetUniformLocation(
                programRef, variableName + ".direction")
        else:
            self.variableRef = glGetUniformLocation(programRef, variableName)

    def upload(self):
        if self.variableRef == -1 or self.variableRef is None:
            return
        if self.dataType == UniformDataType.MAT4:
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)
        elif self.dataType == UniformDataType.VEC4:
            glUniform4f(
                self.variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType == UniformDataType.VEC3:
            glUniform3f(
                self.variableRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType == UniformDataType.VEC2:
            glUniform2f(
                self.variableRef, self.data[0], self.data[1])
        elif self.dataType == UniformDataType.INT:
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == UniformDataType.BOOL:
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == UniformDataType.FLOAT:
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == UniformDataType.SAMPLER2D:
            print("Sampler2D ", self.variableRef, self.data)
            glActiveTexture(GL_TEXTURE0 + self.data)
            glBindTexture(GL_TEXTURE_2D, self.data)
            glUniform1i(self.variableRef, self.data)
        elif self.dataType == UniformDataType.LIGHT:
            glUniform1i(self.variableRef["lightType"], self.data.lightType)
            if(self.data.lightType == Light.DIRECTIONAL):
                glUniform3f(self.variableRef["direction"], self.data.direction[0],
                            self.data.direction[1], self.data.direction[2])
            position = self.data.getPosition()
            glUniform3f(self.variableRef["position"], position[0],
                        position[1], position[2])
            glUniform3f(self.variableRef["color"], self.data.color[0],
                        self.data.color[1], self.data.color[2])
        else:
            raise Exception("Uniform location + " +
                            str(self.variableRef) + " has Unknown data type")
