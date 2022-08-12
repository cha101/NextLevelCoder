import random 

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0 #random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 130

        def draw (self, screen):
            if self.index >=9:
                self.index = 0
            screen.blit(self.image[self.index // 5], self.rect)
            self.index += 1
        #image, bird_type = self. 
        #self.heights = [40, 0, -40, -80]
        #self.height = random.choice(self.heights)
        #self.step_bird += 1

