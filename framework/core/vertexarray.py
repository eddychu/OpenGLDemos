from OpenGL.GL import *


class VertexArray(object):

    def __init__(self) -> None:
        self.handle = glGenVertexArrays(1)

    def bind(self):
        glBindVertexArray(self.handle)

    def unbind(self):
        glBindVertexArray(0)

    def destroy(self):
        glDeleteVertexArrays(1, [self.handle])
