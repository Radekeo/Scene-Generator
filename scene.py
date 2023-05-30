import random
from model import *


MAX = 3

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def load(self):
        locations = self.generate_locations()
        print(locations[0],locations[1])
        # place models
        for i in range(MAX):
            obj = random.choice([0,1])
            match obj:
                case 0: 
                    self.objects.append(Cube(self.app, pos=locations[i]))
                case 1:
                    self.objects.append(Pyramid(self.app, pos=locations[i]))

        # place camera
        # place light

    def render(self):
        for model in self.objects:
            model.draw()

    def generate_locations(self):
        #return a list of MAX number of x,y,z coordinates in a tuple

        k = MAX

        locations = []
        y = -1

        for i in range(k):
            x = round(random.uniform(-8, 8), 2)
            z = round(random.uniform(-2, 1), 2)
            locations.append((x, y, z))

        return locations

    def destroy(self):
        for model in self.objects:
            model.destroy()
        
            