from logging import Handler
from OpenGL.GL import *
from PIL import Image
import numpy


class Texture(object):

    def __init__(self, fileName=None, properties={}) -> None:
        self.data = None
        self.handle = glGenTextures(1)
        self.properties = {
            "magFilter": GL_LINEAR,
            "minFilter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap": GL_REPEAT
        }
        if fileName is not None:
            im = Image.open(fileName).transpose(Image.FLIP_TOP_BOTTOM)
            self.width, self.height = im.size
            im = im.convert("RGBA")
            self.data = numpy.asarray(im, dtype=numpy.uint8)
            print(self.data)

        self.setProperties(properties)
        self.upload()

    def setProperties(self, properties):
        for name, data in properties.items():
            if name in self.properties.keys():
                self.properties[name] = data
            else:
                raise Exception("Texture has no property named: " + name)

    def upload(self):
        glBindTexture(GL_TEXTURE_2D, self.handle)
        glTexStorage2D(GL_TEXTURE_2D, 1, GL_RGBA8, self.width, self.height)
        glTexSubImage2D(GL_TEXTURE_2D, 0, 0, 0, self.width,
                        self.height, GL_RGBA, GL_UNSIGNED_BYTE, self.data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                        self.properties["magFilter"])
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                        self.properties["minFilter"])

    def destroy(self):
        glDeleteTextures(1, self.handle)
