import glfw
from OpenGL.GL import *
from .input import Input


class Base(object):
    def __init__(self, size=[640, 480]) -> None:
        self.size = size
        if not glfw.init():
            return
        # Create a windowed mode window and its OpenGL context
        self.window = glfw.create_window(640, 480, "Hello World", None, None)
        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 6)
        # glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        # glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        if not self.window:
            glfw.terminate()
            return

        self.input = Input()
        # Make the window's context current
        glfw.make_context_current(self.window)

        glfw.set_framebuffer_size_callback(
            self.window, self.framebuffer_size_callback)
        glfw.set_key_callback(self.window, self.key_callback)
        glfw.set_mouse_button_callback(self.window, self.mouse_button_callback)
        glfw.set_cursor_pos_callback(self.window, self.mouse_position_callback)

    def onResize(self, size):
        pass

    def framebuffer_size_callback(self, window, width, height):
        print("check framebuffer size callback " +
              str(width) + " " + str(height))
        glViewport(0, 0, width, height)
        self.size = [width, height]
        self.onResize(self.size)

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            self.input.keyDownList.append(key)
        elif action == glfw.RELEASE:
            self.input.keyDownList.remove(key)
        print("keydown : ", self.input.keyDownList)

    def mouse_button_callback(self, window, button, action, mods):
        print("mouse button callback " + str(button) + " " + str(action))
        if action == glfw.PRESS:
            self.input.mouseButtonDownList.append(button)
        elif action == glfw.RELEASE:
            self.input.mouseButtonDownList.remove(button)

    def mouse_position_callback(self, window, xpos, ypos):
        print("mouse position callback " + str(xpos) + " " + str(ypos))
        self.input.mousePosition = [xpos, ypos]

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while not glfw.window_should_close(self.window):
            if(self.input.isKeyDown(glfw.KEY_ESCAPE)):
                break
            self.update()
            glfw.swap_buffers(self.window)
            glfw.poll_events()
        glfw.terminate()
