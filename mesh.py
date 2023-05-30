from vao import VAO
from texture import Texture
import random


class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)
        self.textures = {}
        self.textures['cube'] = self.texture.textures[random.choice([0,1])]
        self.textures['pyramid'] = self.texture.textures[random.choice([2,3])]

    def destroy(self):
        self.vao.destroy()
        [tex.release() for tex in self.textures.values()]
        self.texture.destroy()
        