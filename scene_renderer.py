import random

from scene import *
from light import *


class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.scene = app.scene

    def render_shadow():
        TODO

    def render(self):
        # self.render_shadow()
        self.scene.render()

    def destroy(self):
       self.scene.destroy()