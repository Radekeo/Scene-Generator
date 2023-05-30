import pygame as pg
import moderngl as mgl
import glm

class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.load_texture('textures/ice.jpg')
        self.textures[1] = self.load_texture('textures/lava.jpg')
        self.textures[2] = self.load_texture('textures/limestone.jpg')
        self.textures[3] = self.load_texture('textures/polkahearts.jpg')

    def load_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        # texture.fill('red')
        texture = self.ctx.texture(size=texture.get_size(), components=3, data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]