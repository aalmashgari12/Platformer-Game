import pygame
from settings import SCREEN_HEIGHT,SCREEN_WIDTH,FPS
from player import Player
from lvl2_background import Background

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Game window')
        self.clock = pygame.time.Clock()
        self.running = True

        animation = {
            'idle':{
                'path': 'Level 2/Character/Idle/Idle-Sheet.png',
                'num_frames': 4,
                'frame_width': 64,
                'frame_height': 80
            },
            'run':{
                'path': 'Level 2/Character/Run/Run-Sheet.png',
                'num_frames': 8,
                'frame_width': 80,
                'frame_height': 80
            },
            'jump':{
                'path': 'Level 2/Character/Jumlp-All/Jump-All-Sheet.png',
                'num_frames': 15,
                'frame_width': 64,
                'frame_height': 64
            },
            'attack':{
                'path': 'Level 2/Character/Attack-01/Attack-01-Sheet.png',
                'num_frames': 8,
                'frame_width': 91,
                'frame_height': 80

            },
            'dead':{
                'path': 'Level 2/Character/Dead/Dead-Sheet.png',
                'num_frames': 8,
                'frame_width': 80,
                'frame_height': 64
            }
        }


        # Initialize the player

        self.player = Player(animation)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Initializing the background

        tile_info = {
            #torch
            0: (25,0,40,45),
            #background
            1: (400,0,105,180),
            #ground
            2: (145,160,50,65),
            #ground without grass
            3: (145,170,50,65),
            #floating ground
            4: (130,55,200,37),
            #rocks
            5: (220,80,30,20),
            #slope
            6: (64,116,65,65)
        }

        tile_map = [
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6],
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 3, 3],
            [1, 1, 1 ,4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 6, 3, 3, 1],
            [1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 3, 3, 3, 3],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 3, 3, 3, 3, 3],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 3, 3, 3, 3, 3],
            [2, 2, 2 ,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3 ,3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        ]

        self.background = Background('Level 2/Pixel_Platformer_Tileset_Pack/Asset_03/pixel_platform_03_tileset_final.png', 50, 50, tile_info, tile_map)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS)
            self.events()
            self.update(dt)
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.all_sprites.update(keys,dt)

    def draw(self):
        # self.window.fill((46,79,21))
        self.background.draw(self.window)
        self.all_sprites.draw(self.window)
        pygame.display.update()

    def quit(self):
        pygame.quit()




