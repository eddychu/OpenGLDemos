from OpenGL.GL import *
import numpy
from enum import Enum


class AttributeDataType(Enum):
    FLOAT = 1
    INT = 2
    VEC2 = 3
    VEC3 = 4
    VEC4 = 5


class Attribute(object):

    def __init__(self, dataType: AttributeDataType, data) -> None:
        self.dataType = dataType
        self.data = data
        self.handle = glGenBuffers(1)
        self.upload()

    def upload(self):
        data = numpy.array(self.data).astype(numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.handle)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    def bindTo(self, location):
        print("dataTYpe", self.dataType)
        glBindBuffer(GL_ARRAY_BUFFER, self.handle)

        if self.dataType == AttributeDataType.FLOAT:
            glVertexAttribPointer(location, 1, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == AttributeDataType.INT:
            glVertexAttribIPointer(location, 1, GL_INT, GL_FALSE, 0, None)
        elif self.dataType == AttributeDataType.VEC2:
            glVertexAttribPointer(location, 2, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == AttributeDataType.VEC3:
            glVertexAttribPointer(location, 3, GL_FLOAT, GL_FALSE, 0, None)
        elif self.dataType == AttributeDataType.VEC4:
            glVertexAttribPointer(location, 4, GL_FLOAT, GL_FALSE, 0, None)
        else:
            raise Exception("Attribute location + " +
                            location + " has Unknown data type")
        glEnableVertexAttribArray(location)
