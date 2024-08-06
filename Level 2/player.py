import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
 
 #crop animations, get new sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, animations):
        super().__init__()
        self.animations = animations
        self.current_animation = 'idle'
        self.frames = self.load_frames(self.animations[self.current_animation])
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.animation_speed = 0.1
        self.animation_timer = 0
        self.is_jumping = False
        self.is_running = False
        self.is_idle = True
        self.is_attack = False
        self.jump_speed = -15
        self.gravity = 1
        self.velocity_y = 0
 
    def load_frames(self, sprite_sheet_info):
        frames = []
        sprite_sheet = pygame.image.load(sprite_sheet_info['path']).convert()
        num_frames = sprite_sheet_info['num_frames']
        frame_width = sprite_sheet_info['frame_width']
        frame_height = sprite_sheet_info['frame_height']
        for i in range(num_frames):
            frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames
 
    def update(self, keys, dt):
        self.handle_input(keys)
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
 
        self.keep_within_screen()
        # self.apply_gravity()
 
 
    def handle_input(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.change_animation('jump')
            self.is_jumping = True
            self.is_running = False
            self.is_idle = False
            self.is_attack = False
            self.velocity_y = self.jump_speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.change_animation('run')
            self.is_jumping = False
            self.is_running = True
            self.is_idle = False
            self.is_attack = False
        elif keys[pygame.K_a] and not self.is_attack:
            self.change_animation('attack')
            self.is_jumping = False
            self.is_running = False
            self.is_idle = False
            self.is_attack = True
        else:
            self.change_animation('idle')
            self.is_jumping = False
            self.is_running = False
            self.is_idle = True
            self.is_attack = False

    def change_animation(self, animation):
        if self.current_animation != animation:
            self.current_animation = animation
            self.frames = self.load_frames(self.animations[self.current_animation])
 
    # def apply_gravity(self):
    #     if self.is_jumping:
    #         self.velocity_y += self.gravity
    #         self.rect.y += self.velocity_y
 
    #         if self.rect.bottom >= SCREEN_HEIGHT:
    #             self.rect.bottom = SCREEN_HEIGHT
    #             self.is_jumping = False
    #             self.velocity_y = 0
 
    def keep_within_screen(self):
        # Keep player within screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
 