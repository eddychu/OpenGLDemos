from OpenGL.GL import *
from numpy import array
from framework.core.camera import Camera
from framework.core.scene import Scene
from framework.core.mesh import Mesh


class Renderer(object):

    def __init__(self, size) -> None:
        self.size = size

    def render(self, scene: Scene, camera: Camera):
        glViewport(0, 0, self.size[0], self.size[1])
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.updateViewMatrix()
        descendants = scene.getDescendantList()
        def meshFilter(x): return isinstance(x, Mesh)
        renderList = list(filter(meshFilter, descendants))

        for mesh in renderList:
            mesh.material.shader.use()
            mesh.vao.bind()
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix

            for variableName, uniformObject in mesh.material.uniforms.items():
                print(variableName)
                print(uniformObject.dataType)
                location = mesh.material.shader.findUniformLocation(
                    variableName)
                print(location)
                if location != -1:
                    uniformObject.bind(location)
            glDrawArrays(
                mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)
