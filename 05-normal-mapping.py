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
from framework.geometry.rectangleGeometry import RectangleGeometry
from framework.material.basicMaterial import BasicMaterial
from framework.material.phoneMaterial import PhongMaterial
from framework.core.texture import Texture
from framework.light.ambientLight import AmbientLight
from framework.light.directionalLight import DirectionalLight
from framework.light.pointLight import PointLight


class Example(Base):
    def __init__(self):
        super().__init__()
        self.name = "02-a-cube"

    def initialize(self):
        print("Initializing {}...".format(self.name))
        self.renderer = Renderer(self.size)
        self.scene = Scene()
        self.camera = Camera(60, self.size[0] / self.size[1], 0.1, 100.0)
        self.camera.setPosition([0.0, 0.0, 3.0])
        cube = BoxGeometry(1, 1, 1)
        texture = Texture("resources/textures/brickwall.jpg")
        normalTexture = Texture("resources/textures/brickwall_normal.jpg")
        # normalTexture = Texture("resources/textures/brickwall_normal.jpg")
        material = PhongMaterial(texture, normalTexture)
        self.mesh = Mesh(cube, material)
        self.scene.add(self.mesh)

        light0 = PointLight([1, 1, 1])
        light0.setPosition([-0.4, 0.4, 1])
        light1 = AmbientLight([1, 1, 1])

        self.scene.add(light0)
        self.scene.add(light1)

        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)

    def onResize(self, size):
        self.renderer.size = size

    def update(self):
        self.mesh.rotateX(0.003)
        self.mesh.rotateY(0.004)
        # self.mesh.rotateX(0.003)
        # self.mesh.rotateY(0.004)
        self.renderer.render(self.scene, self.camera)


if __name__ == "__main__":
    Example().run()
