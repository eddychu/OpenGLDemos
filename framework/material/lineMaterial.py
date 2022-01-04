from framework.material.basicMaterial import BasicMaterial
from OpenGL.GL import *


class LineMaterial(BasicMaterial):

    def __init__(self, properties={}) -> None:
        super().__init__()
        self.settings["drawStyle"] = GL_LINE_STRIP
        self.settings["lineWidth"] = 1.0
        self.settings["lineType"] = "connected"

        self.setProperties(properties)

    def updateRenderSettings(self):
        glLineWidth(self.settings["lineWidth"])
        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown LineMaterial draw style.")
