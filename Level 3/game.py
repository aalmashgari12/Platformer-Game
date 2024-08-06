import pygame
from settings import SCREEN_HEIGHT,SCREEN_WIDTH,FPS
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Game window')
        self.clock = pygame.time.Clock()
        self.running = True

        # Load assets
        self.player_image_path = "Level 2/"


        # Initialize Player
        self.player = Player(self.player_image_path,6,170,180)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Load the background image
        # self.background = self.window.fill(46,79,21)


    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys,500)

    def draw(self):
        self.window.fill((46,79,21))
        self.all_sprites.draw(self.window)
        pygame.display.update()

    def quit(self):
        pygame.quit()