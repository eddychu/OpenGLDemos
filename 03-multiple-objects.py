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
from framework.geometry.planeGeometry import PlaneGeometry
from framework.geometry.sphereGeometry import SphereGeometry


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "03-multiple-objects"

    def initialize(self):
        print("Initializing {}...".format(self.name))
        self.renderer = Renderer(self.size)
        self.scene = Scene()
        self.camera = Camera(60, self.size[0] / self.size[1], 0.1, 100.0)
        self.camera.setPosition([0.0, 0.0, 5.0])
        plane = PlaneGeometry(10, 10)

        material = BasicMaterial()
        self.mesh = Mesh(plane, material)
        self.mesh.rotateX(3.0/2)
        self.mesh.setPosition([0, -2, -1])
        self.scene.add(self.mesh)

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    def onResize(self, size):
        self.renderer.size = size

    def update(self):
        # self.mesh.rotateY(0.0337)
        self.renderer.render(self.scene, self.camera)

    def cleanup(self):
        pass
        # print("Cleaning up {}...".format(self.name))
        # self.positionAttribute.destroy()
        # self.vao.destroy()
        # self.shader.destroy()


if __name__ == "__main__":
    Example().run()
