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
from framework.material.lineMaterial import LineMaterial
from framework.extras.axesHelper import AxesHelper


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "02-a-cube"

    def initialize(self):
        print("Initializing {}...".format(self.name))
        self.renderer = Renderer(self.size)
        self.scene = Scene()
        self.camera = Camera(60, self.size[0] / self.size[1], 0.1, 100.0)
        self.camera.setPosition([10.0, 10.0, 100.0])
        axis = AxesHelper(10)
        # material = BasicMaterial()
        self.scene.add(axis)

    def update(self):
        # self.mesh.rotateX(0.003)
        # self.mesh.rotateY(0.004)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Example().run()
