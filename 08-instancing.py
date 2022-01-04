from framework.core.base import Base
from framework.core.shader import Shader
from framework.core.vertexarray import VertexArray
from framework.core.matrix import Matrix
from framework.core.attribute import AttributeDataType, Attribute
from framework.core.uniform import UniformDataType, Uniform
from OpenGL.GL import *
from framework.core.renderer import Renderer
from framework.core.camera import Camera
from framework.core.mesh import Mesh
from framework.core.scene import Scene
from framework.geometry.boxGeometry import BoxGeometry
from framework.material.basicMaterial import BasicMaterial


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "02-a-cube"

    def initialize(self):
        print("Initializing {}...".format(self.name))
        self.renderer = Renderer(self.size)
        self.scene = Scene()
        self.camera = Camera(60, self.size[0] / self.size[1], 0.1, 100.0)
        self.camera.setPosition([0.0, 0.0, 20.0])
        material = BasicMaterial()
        geometry = BoxGeometry(1, 1, 1)

        instancePositionData = []
        for i in range(10):
            for j in range(10):
                instancePositionData.append(-9.0 + i * 2)
                instancePositionData.append(9.0 - j * 2)
                instancePositionData.append(0.0)

        geometry.addAttribute("instancePosition",
                              AttributeDataType.VEC3, instancePositionData, True)
        self.cube = Mesh(geometry, material, 100)
        self.scene.add(self.cube)
        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)

    def update(self):

        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Example().run()
