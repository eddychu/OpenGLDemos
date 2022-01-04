from framework.core.object3D import Object3D


class OrbitControl(Object3D):

    def __init__(self, camera, target) -> None:
        super().__init__()
        self.children = [camera]
        self.setPosition(camera.getPosition())
        self.target = target
        
