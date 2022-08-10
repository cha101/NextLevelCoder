import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
#from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.step_obstacle = 0
        #self.image = BIRD[0]
        #self.pos_y = 330
        #self.cactus = Cactus()

    def update(self, game):
        if len(self.obstacles) == 0:
            type_list = random.randint(0, 1)
            if type_list == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif type_list == 1:
                #self.pos_y
                #self.cactus.self.rect.y.update(self.pos_y)
                self.obstacles.append(Cactus(LARGE_CACTUS)) 

           # elif type_list == 2:
            #    self.image = BIRD[0] if self.step_obstacle < 5 else BIRD[1]
             #   self.obstacles.append(Bird[0])
              #  self.step_index += 1
                

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
