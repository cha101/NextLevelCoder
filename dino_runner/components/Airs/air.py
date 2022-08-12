
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Air(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, air_obstacles):
        game_speed += 20
        self.rect.x -= game_speed
        if self.rect.x < - self.rect.width:
            air_obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)