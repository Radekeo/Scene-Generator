from vbo import *
from shader import *

class VAO:
    def __init__(self,ctx):
        self.vaos = {}
        self.vaos['cube'] = CubeVAO(ctx)
        self.vaos['pyramid'] = PyramidVAO(ctx)
        # self.vaos['sphere'] = SphereVAO(ctx)
    
    def destroy(self):
        [vao.destroy() for vao in self.vaos.values()]

class BaseVAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.buffer = VBO(ctx)
        self.shader_program = Shader(ctx)
        self.vbo = None
        self.program = None
        self.vao = None

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.shader_program.destroy()
        self.buffer.destroy()
        self.vao.release()
    

class CubeVAO(BaseVAO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.vbo = self.buffer.vbos['cube']
        self.program = self.shader_program.programs['cube']
        self.vao = self.get_vao(self.program, self.vbo)

class PyramidVAO(BaseVAO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.vbo = self.buffer.vbos['pyramid']
        self.program = self.shader_program.programs['pyramid']
        self.vao = self.get_vao(self.program, self.vbo)