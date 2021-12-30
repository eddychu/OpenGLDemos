from framework.core.object3D import Object3D
from framework.core.matrix import Matrix
from numpy.linalg import inv


class Camera(Object3D):

    def __init__(self, fov=60, aspectRatio=1, near=0.1, far=1000.0) -> None:
        super().__init__()
        self.projectionMatrix = Matrix.makePerspective(
            fov, aspectRatio, near, far)
        self.viewMatrix = Matrix.makeIdentify()

    def updateViewMatrix(self):
        self.viewMatrix = inv(self.getWorldMatrix())
