import random 

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 130
        #image, bird_type = self. 
        #self.heights = [40, 0, -40, -80]
        #self.height = random.choice(self.heights)
        #self.step_bird += 1

