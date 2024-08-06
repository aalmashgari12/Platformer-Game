import pygame


class Background():
    def __init__(self,sprite_sheet_path,tile_width,tile_height,tile_info,tile_map,scroll_speed=0):
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_map = tile_map
        self.scroll_speed = scroll_speed
        self.tile_info = tile_info
        self.tiles = self.load_tiles()
        self.background = self.blit_tiles()
    
    def load_tiles(self):
        tiles = {}
        for tile_id, (x,y,width,height) in self.tile_info.items():
            tile = self.sprite_sheet.subsurface((x,y,width,height))
            tiles[tile_id] = tile
        return tiles

        
    def blit_tiles(self):
        rows = len(self.tile_map)
        cols = len(self.tile_map[0])
        tile_width, tile_height = self.tile_info[0][2], self.tile_info[0][3]
        background_surface = pygame.Surface((cols*tile_width, rows*tile_height))
        for row in range(rows):
            for col in range(cols):
                tile_id = self.tile_map[row][col]
                if tile_id != -1:
                    tile = self.tiles[tile_id]
                    background_surface.blit(tile, (col*tile_width, row*tile_height))
        return background_surface

    

    def draw(self, screen):
        screen.blit(self.background, (0,0))

                
                

    