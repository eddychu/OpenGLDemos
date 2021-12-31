from framework.light.light import Light


class PointLight(Light):
    def __init__(self, color=[1, 1, 1]):
        super().__init__(Light.POINT)
        self.color = color
