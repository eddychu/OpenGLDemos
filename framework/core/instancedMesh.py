from framework.core.mesh import Mesh


class InstancedMesh(Mesh):

    def __init__(self, geometry, material, count=1) -> None:
        super().__init__(geometry, material)
        self.count = count
