from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image, self.type)
        self.rect.y = 330