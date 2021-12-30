import glfw


class Input(object):

    def __init__(self) -> None:
        self.keyDownList = []
        self.mouseButtonDownList = []
        self.mousePosition = [0, 0]

    def isKeyDown(self, key):
        return key in self.keyDownList
