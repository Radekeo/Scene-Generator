import numpy as np
import glm
import random

from mesh import *

class BaseModel:
    def __init__(self, app, pos):
        self.app = app
        self.ctx = app.ctx
        self.pos = pos
        self.m_matrix = self.get_model_matrix()
    
    def get_model_matrix(self):
        m_matrix = glm.mat4()
        # translate
        m_matrix = glm.translate(m_matrix, self.pos)

        return m_matrix

    def update(self): ...

    def draw(self):
        self.update()
        self.vao.vao.render()

    def destroy(self):
        self.vao.vao.release()


class Cube(BaseModel):
    def __init__(self, app, pos):
        super().__init__(app, pos)
        self.vao = app.mesh.vao.vaos['cube']
        self.program = self.vao.program
        self.texture = app.mesh.textures['cube']
        self.oninit()

    def oninit(self):
        # Texture
        self.program['u_texture_0'] = 0
        self.texture.use(0)

        # MVP
        self.program['m_matrix'].write(self.m_matrix)
        self.program['v_matrix'].write(self.app.camera.v_matrix)
        self.program['p_matrix'].write(self.app.camera.p_matrix)

        # Light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

        self.program['camPos'].write(self.app.camera.position)

    def update(self):
        m_matrix = glm.rotate(self.m_matrix, self.app.time * 0.5, glm.vec3(0,1,0))
        self.program['m_matrix'].write(m_matrix)
        self.program['v_matrix'].write(self.app.camera.v_matrix)
        self.program['camPos'].write(self.app.camera.position)

class Pyramid(BaseModel):
    def __init__(self, app, pos):
        super().__init__(app, pos)
        self.vao = app.mesh.vao.vaos['pyramid']
        self.program = self.vao.program
        self.texture = app.mesh.textures['pyramid']
        self.oninit()

    def oninit(self):
        # Texture
        self.program['u_texture_1'] = 1
        self.texture.use(1)
        
        # MVP
        self.program['m_matrix'].write(self.m_matrix)
        self.program['v_matrix'].write(self.app.camera.v_matrix)
        self.program['p_matrix'].write(self.app.camera.p_matrix)

        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

        self.program['camPos'].write(self.app.camera.position)

    def update(self):
        m_matrix = glm.rotate(self.m_matrix, self.app.time * 0.5, glm.vec3(0,1,0))
        self.program['m_matrix'].write(m_matrix)
        self.program['v_matrix'].write(self.app.camera.v_matrix)
        self.program['camPos'].write(self.app.camera.position)

    
