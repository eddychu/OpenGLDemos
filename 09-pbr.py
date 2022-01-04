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
from framework.material.pbrMaterial import PBRMaterial
from framework.light.pointLight import PointLight

# there is issue with this example
# when rotating. it seems that the light is also rotating
# need add helper line drawing utility to draw normal and light lines for debug purposes


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "02-a-cube"

    def initialize(self):
        print("Initializing {}...".format(self.name))
        self.renderer = Renderer(self.size)
        self.scene = Scene()
        self.camera = Camera(60, self.size[0] / self.size[1], 0.1, 100.0)
        self.camera.setPosition([0.0, 0.0, 5.0])
        cube = BoxGeometry(1, 1, 1)
        material = PBRMaterial()
        self.mesh = Mesh(cube, material)
        light = PointLight([10, 10, 10])
        light.setPosition([1, 1, 3])
        self.scene.add(self.mesh)
        self.scene.add(light)
        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)

    def update(self):

        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Example().run()
