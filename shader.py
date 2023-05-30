class Shader:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['cube'] = self.load_program('cube')
        self.programs['pyramid'] = self.load_program('pyramid')
        

    def load_program(self, shader_name):
        with open(f'shaders/verts/{shader_name}.vert') as f:
            vertex_shader = f.read()

        with open(f'shaders/frags/{shader_name}.frag') as f:
            fragment_shader = f.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]