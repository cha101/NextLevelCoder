import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

FONT_STYLE = 'freesansbold.ttf'

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
    
    def update_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
        self.message(f"Points: {self.points}", 30, 1000, 50)

    def reset(self):
        self.game_speed = 20
        self.points = 0
        #self.death_count += 1
    
    def message(self, message, characters_size, rect_x, rect_y):
        font = pygame.font.Font(FONT_STYLE, characters_size)
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (rect_x, rect_y)
        self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.K_DOWN:
                self.playing = False
                self.running = False 
                pygame.display.quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                self.reset()
                self.run()                

    def show_menu(self):
        self.screen.fill((250, 250, 250))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_widht = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.message("Press any key to start", 30, half_screen_widht, half_screen_height)
        elif self.death_count > 0:
            #self.message("Press DOWN to close \n" f"Score: {self.points}\n" f"Deaths: {self.death_count}", 30, half_screen_widht, half_screen_height) 
            self.message("YOU CRASHED", 50, half_screen_widht, half_screen_height)
            self.message(f"Score: {self.points}", 30, half_screen_widht, half_screen_height + 50)
            self.message(f"Deaths: {self.death_count}", 20, half_screen_widht, half_screen_height + 80)
            self.message("If you want to EXIT press DOWN", 22, half_screen_widht, half_screen_height + 125)
            self.message("otherwise any other key", 32, half_screen_widht, half_screen_height + 160)

        self.screen.blit(RUNNING[0], (half_screen_widht - 20, half_screen_height - 140))

        pygame.display.update()
        self.handle_key_events_on_menu()
