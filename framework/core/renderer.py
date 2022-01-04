from OpenGL.GL import *
from numpy import array
from framework.core.camera import Camera
from framework.core.scene import Scene
from framework.core.mesh import Mesh
from framework.light.light import Light


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

        def lightFilter(x): return isinstance(x, Light)
        lightList = list(filter(lightFilter, descendants))
        while len(lightList) < 4:
            lightList.append(Light())

        for mesh in renderList:
            mesh.material.shader.use()
            mesh.vao.bind()
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix

            if "light0" in mesh.material.uniforms.keys():
                for lightNumber in range(4):
                    lightName = "light" + str(lightNumber)
                    lightObject = lightList[lightNumber]
                    mesh.material.uniforms[lightName].data = lightObject

            if "viewPostion" in mesh.material.uniforms.keys():
                mesh.material.uniforms["viewPostion"].data = camera.getWorldPosition(
                )
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.upload()

            if mesh.geometry.index is not None:
                if mesh.count > 1:
                    glDrawElementsInstanced(
                        mesh.material.settings["drawStyle"], mesh.geometry.vertexCount, GL_UNSIGNED_INT, None, mesh.count)
                else:
                    glDrawElements(
                        mesh.material.settings["drawStyle"], mesh.geometry.vertexCount, GL_UNSIGNED_INT, None)
            else:
                if mesh.count > 1:
                    print("drawing instanced ", mesh.count)
                    glDrawArraysInstanced(
                        mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount, mesh.count)
                else:
                    glDrawArrays(
                        mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)
