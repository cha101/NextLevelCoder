import random 

from dino_runner.components.Airs.air import Air

class Pterodactyl(Air):
    def __init__(self, image):
        self.family = "bird"
        self.type = 0
        self.height = random.choice[ 300, 275, 250, 225, 200, 175, 150, 125, 100, 75, 50, 25, 0]
        super().__init__(image, self.type)
        self.rect.y = self.height