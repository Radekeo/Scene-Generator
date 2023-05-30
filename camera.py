import glm
import pygame as pg

FOV = 50 #deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.04


class Camera:
    def __init__(self, app, position=(0, 0, 7), yaw=-90, pitch=0):
        self.app = app
        self.ar = app.width/app.height

        # position and angles
        self.position = glm.vec3(position)
        self.yaw = yaw
        self.pitch = pitch
        
        # up, right and forward
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        # view matrix
        self.v_matrix = self.get_view_matrix()

        # projection matrix
        self.p_matrix = self.get_projection_matrix()


    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def move(self):
        velocity = SPEED * self.app.deltatime
        keys = pg.key.get_pressed()

        #wasd = up, left, down, right. qe= out, in
        if  keys[pg.K_w] or keys[pg.K_UP]:
            self.position -= velocity * self.up
        elif keys[pg.K_s] or keys[pg.K_DOWN]:
            self.position += velocity * self.up
        elif keys[pg.K_a] or keys[pg.K_LEFT]:
            self.position += velocity * self.right
        elif keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.position -= velocity * self.right
        elif keys[pg.K_q]:
            self.position -= velocity * self.forward
        elif keys[pg.K_e]:
            self.position += velocity * self.forward

    def update(self):
        self.move()
        self.v_matrix = self.get_view_matrix()
        

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.ar, NEAR, FAR)