
import numba
import numpy
import OpenGL.GL as OpenGL
import glfw as GLFW
import platform
import os

from lib.math.Point import Point
from lib.jitted.update import update_entity
from lib.jitted.pre_render import pre_render
from lib.matter.Water import Water

class App:
    env = platform.system()

    @staticmethod
    def os_pick(value1, value2):
        return value2 if App.env == 'Darwin' else value1

    def __init__(self, title, width, height) -> None:

        del os.environ['DISPLAY']

        self.title = title
        self.width = width
        self.height = height
        self.time = 0
        self.buffer = numpy.zeros(self.width * self.height * 3, int)
        self.clear_color = (0, 0, 0, 255) # black

        self.entity_instances = [] # real
        self.entities = numpy.array([], int)

        GLFW.init()

        self.window = GLFW.create_window(
            App.os_pick(width, width // 2),
            App.os_pick(height, height // 2),
            self.title,
            None,
            None
        )

        GLFW.make_context_current(self.window)
        GLFW.set_mouse_button_callback(
            self.window, 
            lambda _, button, action, __: self.on_click(button, action)
        )
        GLFW.set_cursor_pos_callback(
            self.window,
            lambda _, x, y: self.on_move(Point(x, y))
        )

        if self.env == 'Darwin':
            buf_width, buf_height = GLFW.get_framebuffer_size(self.window)
            OpenGL.glViewport(
                -(self.width - buf_width) // 2,
                -(self.height - buf_height) // 2,
                self.width,
                self.height
            )
        else:
            OpenGL.glViewport(0, 0, self.width, self.height)

        
        OpenGL.glMatrixMode(OpenGL.GL_PROJECTION)
        OpenGL.glLoadIdentity()
        OpenGL.glOrtho(0, self.width, 0, self.height, 0, 10)
        OpenGL.glPixelZoom(1, -1)
        OpenGL.glRasterPos3f(0, self.height, -0.3)

        while not GLFW.window_should_close(self.window):
            self.tick()
            self.time += 1
        GLFW.terminate()

    def tick(self):
        self.update()
        self.pre_render()
        self.render()
    # 모든 입자에 대한 업데이트
    def update(self):
        self.entities = update_entity(self.entities, self.time)
    # 이 단계에서 buffer에 대한 전체적인 접근과 수정이 이루어진다.
    def pre_render(self):
        self.buffer = pre_render(self.width, self.entities, self.buffer)
    def render(self):
        OpenGL.glClearColor(*self.clear_color)
        OpenGL.glClear(OpenGL.GL_COLOR_BUFFER_BIT)

        OpenGL.glDrawPixels(
            self.width,
            self.height,
            OpenGL.GL_RGB,
            OpenGL.GL_UNSIGNED_BYTE,
            self.buffer
        )

        GLFW.swap_buffers(self.window)
        GLFW.poll_events()

    def on_click(self, button, action):
        pass
    def on_move(self, pos):
        water = Water()
        water.engine = self
        water.x = pos.x
        water.y = pos.y

        self.add(water)

    def add(self, entity):
        # 유기적인 관계를 보존하기 위함
        self.entity_instances.append(entity)

        # simplify
        #self.entities.append(entity.type)
        #self.entities.append(entity.x)
        #self.entities.append(entity.y)
        #self.entities.append(entity.color)

        self.entities = numpy.append(
            self.entities, 
            [
                entity.type, entity.x, entity.y, 

                entity.color[0], entity.color[1], entity.color[2]
            ]
        )
app = App("Lesser Flower", 800, 600)
