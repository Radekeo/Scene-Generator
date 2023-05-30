import pygame as pg
import moderngl as mgl
import sys

from model import *
from camera import *
from light import *
from scene_renderer import SceneRenderer
from scene import *

from vao import *
from mesh import *

RAND_COLOR = random.choice(['white', 'red', 'blue', 'green'])

class GraphicsEngine:
    def __init__(self, win_size=(1280, 720)):
        # initialize pygame modules
        pg.init()
        self.win_size = self.width, self.height = win_size
        self.time = 0
        self.deltatime = 0

        # OpenGL Attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        # Create OpenGL Context
        pg.display.set_mode(self.win_size, flags=pg.OPENGL | pg.DOUBLEBUF | pg.RESIZABLE)
        
        # Use OpenGL Context
        self.ctx = mgl.create_context()
        # Enable Depth Test
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        # Create object to track time
        self.clock = pg.time.Clock()

        self.light = Light().lights[RAND_COLOR]
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)   
        self.scene_renderer = SceneRenderer(self)
        

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
   

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.deltatime = self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()

        


