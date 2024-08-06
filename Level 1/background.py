import pygame
import sys

pygame.init()

width = 500
height = 500
font = pygame.font.SysFont(None, 40)
window = pygame.display.set_mode((width,height))

fps = pygame.time.Clock()

dungeon_tileset = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/character and tileset/Dungeon_Tileset.png').convert_alpha()

torch_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/torch/torch_1.png')

chest_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/chest/chest_1.png')

mini_chest_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/mini_chest/mini_chest_1.png')

horizontal_open_flame_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/flamethrower/flamethrower_1_2.png')

horizontal_closed_flame_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/flamethrower/flamethrower_1_4.png')

vertical_open_flame_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/flamethrower/flamethrower_2_2.png')

vertical_closed_flame_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/flamethrower/flamethrower_2_4.png')

open_peaks_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/peaks/peaks_1.png')

close_peaks_img = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/peaks/peaks_3.png')

key_img_1 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/keys/keys_1_1.png')

key_img_2 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/keys/keys_1_2.png')

key_img_3 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/keys/keys_1_3.png')

key_img_4 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/keys/keys_1_4.png')

coin_img_1 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/coin/coin_1.png')

coin_img_2 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/coin/coin_2.png')

coin_img_3 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/coin/coin_3.png')

coin_img_4 = pygame.image.load('Level 1/2D Pixel Dungeon Asset Pack/items and trap_animation/coin/coin_4.png')

row = 0.2
no_frames = 2
frame_height = 60
frame_width = 48
scale_factor = 3



def section_of_img(background,row,no_frames,frame_height,frame_width,scale_factor,crop_side='None',crop_num=0):
    frames_info = list()
    subsurfaces = list()
    enlarged_subsurface = list()
        
    bg = background

    for col in range(no_frames):
        frames_info.append((col*frame_width,row*frame_height,frame_width,frame_height))

    for info in frames_info:
        rect = pygame.Rect(info)
        subsurface = bg.subsurface(rect)

        if crop_side == 'left':
            cropped_subsurface = subsurface.subsurface((crop_num, 0, frame_width - crop_num, frame_height))
        elif crop_side == 'right':
            cropped_subsurface = subsurface.subsurface((0, 0, frame_width - crop_num, frame_height))
        elif crop_side == 'top':
            cropped_subsurface = subsurface.subsurface((0, crop_num, frame_width, frame_height-crop_num))
        elif crop_side == 'right':
            cropped_subsurface = subsurface.subsurface((0, 0, frame_width, frame_height-crop_num))
        else:  # 'none'
            cropped_subsurface = subsurface
        
        subsurfaces.append(cropped_subsurface)

    for subsurface in subsurfaces:
        enlarge =  pygame.transform.scale(subsurface, (frame_width*scale_factor,frame_height*scale_factor))
        enlarged_subsurface.append(enlarge)
        
    return enlarged_subsurface

#box
box = section_of_img(dungeon_tileset,0.2, 2, 65,50, 3,'right',3)
#small box
small_box = section_of_img(dungeon_tileset,0.2, 2, 65, 50, 1.5,'right',10)
#path
path = section_of_img(dungeon_tileset,1.6, 2, 50, 60,1.5)
#short path
path_2 = section_of_img(dungeon_tileset,0.2, 1, 20, 25, 1.5,'left',10)
#wood
wood = section_of_img(dungeon_tileset,0.01, 1, 15, 80, 1.2,'left',10)
#torch
torch = section_of_img(torch_img, 0.4, 2, 9, 7, 2.5) 
#chest
chest = section_of_img(chest_img, 0.4, 1, 11, 13, 2)
#mini_chest
mini_chest = section_of_img(mini_chest_img, 0.4, 1, 11, 13, 2)
#open and closed flame horizontal and vertical
horizontal_open_flame = section_of_img(horizontal_open_flame_img, 0.4, 1, 23, 16, 2)
horizontal_closed_flame = section_of_img(horizontal_closed_flame_img, 0.4, 1, 23, 16, 2)

#peaks
open_peaks = section_of_img(open_peaks_img, 0.2, 1, 14, 13, 2)
close_peaks = section_of_img(close_peaks_img, 0.2, 1, 14, 13, 2)

#keys

key_1 = section_of_img(key_img_1, 0.2, 1, 10, 15, 2)
key_2 = section_of_img(key_img_2, 0.2, 1, 10, 15, 2)
key_3 = section_of_img(key_img_3, 0.2, 1, 10, 15, 2)
key_4 = section_of_img(key_img_4, 0.2, 1, 10, 15, 2)

#coin

coin_1 = section_of_img(coin_img_1, 0.2, 1, 10, 15, 2)
coin_2 = section_of_img(coin_img_2, 0.2, 1, 10, 15, 2)
coin_3 = section_of_img(coin_img_3, 0.2, 1, 10, 15, 2)
coin_4 = section_of_img(coin_img_4, 0.2, 1, 10, 15, 2)

def background():
    # Rooms
    window.blit(box[0],(0*100,0))
    window.blit(box[1],(1*100,0)) 
    window.blit(box[0],(2*100,0))
    window.blit(box[1],(3*100,0))

    window.blit(small_box[0],(40,200))
    window.blit(small_box[1],(100,200))

    # Paths
    window.blit(pygame.transform.flip(path[0], False, True),(0,3.5*100))
    window.blit(path[0],(0,3.2*100))
    window.blit(pygame.transform.flip(path[0], False, True),(80,3.5*100))
    window.blit(path[0],(80,3.2*100))
    window.blit(pygame.transform.flip(path[0], False, True),(160,3.5*100))
    window.blit(path[0],(160,3.2*100))
    window.blit(pygame.transform.flip(path[0], False, True),(240,3.5*100))
    window.blit(path[0],(240,3.2*100))
    window.blit(pygame.transform.rotate(path[0],90),(260,2.4*100))
    window.blit(pygame.transform.rotate(path[0],90),(260,1.6*100))
    window.blit(pygame.transform.rotate(path[0],-90),(290,2.4*100))
    window.blit(pygame.transform.rotate(path[0],-90),(290,1.6*100))
    window.blit(pygame.transform.rotate(path[0],-90),(290,3.1*100))

    window.blit(pygame.transform.flip(path[0], False, True),(0,3.5*100))
    window.blit(path[0],(0,3.2*100))

    # Short paths (wooden)
    window.blit(pygame.transform.rotate(path_2[0],-90),(1.99*100,60))
    window.blit(pygame.transform.rotate(path_2[0],90),(1.99*100,110))
    window.blit(pygame.transform.rotate(path_2[0],-180), (115,175))
    window.blit(pygame.transform.rotate(path_2[0], -360), (75,175))

    window.blit(wood[0],(270,405))

    #Items and traps
    window.blit(torch[1],(50,90))
    window.blit(torch[1],(50,40))
    window.blit(torch[1],(250,120))
    window.blit(torch[1],(250,40))

    window.blit(chest[0],(100,240))
    window.blit(mini_chest[0],(300,60))

    window.blit(pygame.transform.rotate(horizontal_closed_flame[0],-90),(90,175))


    window.blit(horizontal_closed_flame[0],(200,75))

    window.blit(open_peaks[0],(100,123))
    window.blit(open_peaks[0],(70,123))
    window.blit(open_peaks[0],(130,123))
    window.blit(close_peaks[0],(100,123))
    window.blit(close_peaks[0],(70,123))
    window.blit(close_peaks[0],(130,123))

    window.blit(close_peaks[0],(240,350))
    window.blit(close_peaks[0],(240,375))

sprite = pygame.image.load('Level 1/Sprites1.png')




def run_attack():
    sprite_row = 5
    no_frames_sprite = 6
    frame_width_sprite = 173
    frame_height_sprite = 195

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,sprite_row*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))

    return frames_sprite
    
def jump():
    sprite_row = 2
    no_frames_sprite = 6
    frame_width_sprite = 170
    frame_height_sprite = 205

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,sprite_row*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))

    return frames_sprite

def punch():
    sprite_row = 3
    no_frames_sprite = 6
    frame_width_sprite = 173
    frame_height_sprite = 195

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,sprite_row*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))

    return frames_sprite

def run():
    sprite_row = 4
    no_frames_sprite = 6
    frame_width_sprite = 173
    frame_height_sprite = 195

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,sprite_row*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))

    return frames_sprite

def idle():
    sprite_row = 1
    no_frames_sprite = 6
    frame_width_sprite = 170
    frame_height_sprite = 180

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,(sprite_row+0.5)*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))
    frames_sprite.pop(-1)
    # print("IDLE: ", frames_sprite)
    return frames_sprite

def hurt():
    sprite_row = 1
    no_frames_sprite = 5
    frame_width_sprite = 178
    frame_height_sprite = 195

    frame_info_sprite = list()
    frames_sprite = list()


    for col in range(no_frames_sprite):
        frame_info_sprite.append((col*frame_width_sprite,(sprite_row-0.7)*frame_height_sprite,frame_width_sprite,frame_height_sprite))

    for info in frame_info_sprite:
        frames_sprite.append(sprite.subsurface(pygame.Rect(info)))

    frames_sprite.pop(0)
    return frames_sprite

def draw_text(text,font,color,surface,x,y):
    text = font.render(text,True,color)
    rectangle = text.get_rect()
    rectangle.center = (x,y)
    surface.blit(text,rectangle)

def start():
    start_window = pygame.display.set_mode((width,height))
    start_window.fill((10,56,0))
    start_button = pygame.Rect(140, 200, 200, 40)
    pygame.draw.rect(start_window, (255,255,255),start_button)
    draw_text('Start Game', font, (0,0,0), start_window, 230, 220)
    return start_button


def end():
    window.fill((10,20,120))
    draw_text("Game Over!", font, (210,20,100), window, 240, 100)
    restart_button = pygame.Rect(150, 200, 150, 40)
    pygame.draw.rect(window,(255,255,255),restart_button)
    quit_button = pygame.Rect(155, 255, 150, 35)
    pygame.draw.rect(window,(255,255,255),quit_button)
    draw_text("Play again", font, (0,0,0), window, 220, 215)
    draw_text("Quit", font, (0,0,0), window, 210, 280)
    pygame.display.update()
    return quit_button,restart_button


frame_index = 0
frame_counter = 0
animation_speed = 20
pos_x = 10
pos_y = 310

def run_movement(direction = "Right",status = True):
    global frame_counter,frame_index,animation_speed
    frame_counter += 1

    if frame_index == len(run())-1:
        frame_index = 0

    if frame_counter == animation_speed:
        frame_counter = 0
        frame_index += 1

    current_frame = run()[frame_index]


    if direction == 'Left':
        current_frame = pygame.transform.flip(current_frame,True,False)

    if status: 
        window.blit(pygame.transform.scale(current_frame,(100,100)),(pos_x,pos_y))
    else:
        return None
    return current_frame

def idle_movement(status=True):
    global frame_counter,frame_index,animation_speed
    frame_counter += 1

    if frame_index == len(idle())-1:
        frame_index = 0

    if frame_counter == animation_speed:
        frame_counter = 0
        frame_index += 1

    current_frame = idle()[frame_index]
    # print("idle_movement: ", idle())
    if status: 
        window.blit(pygame.transform.scale(current_frame,(100,100)),(pos_x,pos_y))
    else:
        return None
    return current_frame

def run_attack_movement(direction='Right',status=True):
    global frame_counter,frame_index,animation_speed
    frame_counter += 1

    if frame_index == len(run_attack())-1:
        frame_index = 0

    if frame_counter == animation_speed:
        frame_counter = 0
        frame_index += 1

    current_frame = run_attack()[frame_index]

    if direction == 'Left':
        current_frame = pygame.transform.flip(current_frame,True,False)

    if status: 
        window.blit(pygame.transform.scale(current_frame,(100,100)),(pos_x,pos_y))
    else:
        return None
    return current_frame

max_health = 100
current_health = 100
bar_length = 100
bar_height = 10
bar_size = 10
lives = 10

peak_rect_1 = pygame.Rect(100, 123, 25, 25)
peak_rect_2 = pygame.Rect(70, 123, 25, 25)
peak_rect_3 = pygame.Rect(130, 123, 25, 25)
peak_rect_4 = pygame.Rect(243, 350, 22, 25)
peak_rect_5 = pygame.Rect(243, 375, 22, 25)
flame_h = pygame.Rect(90,175,50,25)
flame_v = pygame.Rect(200,75,28,50)
key_rect = pygame.Rect(295,40,15,10)
chest_rect = pygame.Rect(100,240,13,11)

def health_bar(surface,x,y,current_health,lives):
    # ratio_health = current_health/max_health
    current_health_bar = bar_size*lives
    #empty health
    health_empty = pygame.draw.rect(surface, (255,0,0), (x,y,bar_length,bar_height))
    # current health
    health_current = pygame.draw.rect(surface, (0,255,0), (x,y,current_health_bar,bar_height))
    return health_current,health_empty 


time_s = 0
time_key = 0
time_c = 0
running = True
move_x = 0
move_y = 0
trap_open = False
player_hit = False
key_hit = False
chest_hit = False


statuss = True
direction_player = "Right"
attack_status = False
status_run = False

running = True

def main():
    global running,frame_counter,frame_index,animation_speed,pos_x,pos_y,time_s,key_hit,chest_hit,chest_rect,time_c
    global move_x,move_y,trap_open,lives,statuss,direction_player,player_hit,attack_status,status_run,time_key
    while running:
        window.fill((34,19,26))
        background()
        current_frame = idle_movement(statuss)
        current_frame = run_movement(direction = direction_player, status=status_run)
        current_frame = run_attack_movement(direction = direction_player, status=attack_status)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    move_y += 1
                    move_x = 0
                    statuss = False
                    attack_status = False
                    status_run = True
                if event.key == pygame.K_LEFT:
                    move_x -= 1
                    move_y = 0
                    statuss = False
                    status_run = True
                    attack_status = False
                    direction_player = "Left"
                if event.key == pygame.K_RIGHT:
                    move_x += 1
                    move_y = 0
                    statuss = False
                    attack_status = False
                    status_run = True
                if event.key == pygame.K_a:
                    attack_status = True
                    statuss = False
                    status_run = False
                if event.key == pygame.K_UP:
                    move_y -= 1
                    move_x = 0
                    statuss = False
                    attack_status = False
                    status_run = True
                
            if event.type == pygame.KEYUP:               
                move_y = 0
                move_x = 0
                statuss = True
                status_run = False
                direction_player = "Right"
                attack_status = False

        pos_x += move_x
        pos_y += move_y
        time_s += 1
        player_rect = pygame.Rect(pos_x, pos_y, 100, 100)
        trap_rects = [peak_rect_1, peak_rect_2, peak_rect_3, peak_rect_4, peak_rect_5,flame_h, flame_v]
        if player_rect.colliderect(key_rect):
            key_hit = True
        
        if player_rect.colliderect(chest_rect) and key_hit:
            time_c = 0
            chest_hit = True
            print('Coin collected!')


        if not key_hit:
            time_key += 1
            if time_key >= 0 and time_key < 50:
                window.blit(key_1[0], (295,40))
            elif time_key >= 50 and time_key < 100:
                window.blit(key_2[0], (295,40))
            elif time_key >= 100 and time_key < 150:
                window.blit(key_3[0], (295,40))
            elif time_key >= 150:
                window.blit(key_4[0], (295,40))
                time_key = 0
        else:
            time_key = 0

        if not chest_hit:
            time_c += 1
            if time_c >= 0 and time_c < 50:
                window.blit(coin_1[0], (100,245))
            elif time_c >= 50 and time_c < 100:
                window.blit(coin_2[0], (100,245))
            elif time_c >= 100 and time_c < 150:
                window.blit(coin_3[0], (100,245))
            elif time_c >= 150:
                window.blit(coin_4[0], (100,245))
                time_c = 0




        if time_s >= 530 and time_s < 700:
            trap_open = True
            window.blit(pygame.transform.rotate(horizontal_open_flame[0],-90),(90,175))
            window.blit(horizontal_open_flame[0],(200,75))
            window.blit(open_peaks[0],(100,123))
            window.blit(open_peaks[0],(70,123))
            window.blit(open_peaks[0],(130,123))
            window.blit(open_peaks[0],(240,350))
            window.blit(open_peaks[0],(240,375))
        elif time_s >= 700:
            trap_open = False
            time_s = 0

        if trap_open and not player_hit:
            for trap in trap_rects:
                if player_rect.colliderect(trap):
                    lives -= 2
                    player_hit = True
                    break

        if not trap_open:
            player_hit = False
        

        health_bar(window,pos_x, (pos_y-20), current_health, lives)
        pygame.display.update()
        fps.tick(200)
        if lives <= 0:
            return False

        


game_state = "start"
start_button = start()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "start":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    game_state = "main"
                    pos_x = 10
                    pos_y = 310
                    lives = 10

        elif game_state == "end":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button.collidepoint(event.pos):
                    game_state = "main"
                    pos_x = 10
                    pos_y = 310
                    lives = 10
                if quit_button.collidepoint(event.pos):
                    running = False
        if game_state == "main":
            if not main():
                game_state = "end"
                quit_button,restart_button = end()

    pygame.display.update()
    fps.tick(60)

pygame.quit()
sys.exit()
