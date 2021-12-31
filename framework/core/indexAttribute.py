from OpenGL.GL import *
import numpy


class IndexAttribute(object):
    def __init__(self, data):
        self.handle = glGenBuffers(1)
        self.data = data
        self.upload()

    def bind(self):
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.handle)

    def upload(self):
        data = numpy.array(self.data).astype(numpy.uint32)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.handle)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)
