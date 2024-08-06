import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
 
 #crop animations, get new sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, num_frames, frame_width, frame_height):
        super().__init__()
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.num_frames = num_frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frames = self.load_frames()
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
        self.jump_speed = -15
        self.gravity = 1
        self.velocity_y = 0
 
    def load_frames(self):
        frames = []
        for i in range(self.num_frames):
            frame = self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            frames.append(frame)
        return frames
 
    def update(self, keys, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.num_frames
            self.image = self.frames[self.current_frame]
 
        self.handle_input(keys)
        self.apply_gravity()
 
        if self.is_jumping:
            self.jump()
        elif self.is_running:
            self.run()
        elif self.is_idle:
            self.idle()
 
        self.keep_within_screen()
 
    def handle_input(self, keys):
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.is_running = False
            self.is_idle = False
            self.velocity_y = self.jump_speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.is_jumping = False
            self.is_running = True
            self.is_idle = False
        else:
            self.is_jumping = False
            self.is_running = False
            self.is_idle = True
 
    def apply_gravity(self):
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y
 
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                self.is_jumping = False
                self.velocity_y = 0
 
    def jump(self):
        # Update jump animation frames
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image = self.frames[self.current_frame]
 
    def run(self):
        # Update run animation frames
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image = self.frames[self.current_frame]
 
    def idle(self):
        # Update idle animation frames
        self.current_frame = (self.current_frame + 1) % self.num_frames
        self.image = self.frames[self.current_frame]
 
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
 