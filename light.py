import glm

class Light:
    def __init__(self):
        self.position = (50,50,-10)
        self.lights = {}
        self.lights['white'] = Lighting(self.position, color=(1, 1, 1))
        self.lights['red'] = Lighting(self.position, color=(0.67, 0.05, 0.05))
        self.lights['blue'] = Lighting(self.position, color=(0.52, 0.8, 0.92))
        self.lights['green'] = Lighting(self.position, color=(0, 0.2, 0.3))


class Lighting:
    def __init__(self, position, color):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.06 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
        # view matrix
        self.v_matrix = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))