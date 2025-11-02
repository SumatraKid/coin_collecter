import pygame

class Tilemap:
    def __init__(self, tile_size, tile_x, tile_y, file_path):
        with open(file_path, 'r') as file:
            self.tilemap = []
            for line in file:
                row = [str(tile) for tile in line.strip().split()]
                self.tilemap.append(row)

        self.tile_size = tile_size
        self.tile_x = tile_x
        self.tile_y = tile_y

        # grass images
        self.grass_mid = pygame.image.load("data/sprites/tiles/grass_mid.png").convert()
        self.grass_mid.set_colorkey((0, 0, 0))

        self.grass_right = pygame.image.load("data/sprites/tiles/grass_right.png").convert()
        self.grass_right.set_colorkey((0, 0, 0))

        self.grass_left = pygame.image.load("data/sprites/tiles/grass_left.png").convert()
        self.grass_left.set_colorkey((0, 0, 0))

        # dirt images
        self.dirt_mid = pygame.image.load("data/sprites/tiles/dirt_mid.png").convert()
        
        self.dirt_right = pygame.image.load("data/sprites/tiles/dirt_right.png").convert()
        self.dirt_right.set_colorkey((0, 0, 0))

        self.dirt_left = pygame.image.load("data/sprites/tiles/dirt_left.png").convert()
        self.dirt_left.set_colorkey((0, 0, 0))

        # bottom images
        self.bottom_mid = pygame.image.load("data/sprites/tiles/bottom_mid.png").convert()
        self.bottom_mid.set_colorkey((0, 0, 0))
        
        self.bottom_right = pygame.image.load("data/sprites/tiles/bottom_right.png").convert()
        self.bottom_right.set_colorkey((0, 0, 0))

        self.bottom_left = pygame.image.load("data/sprites/tiles/bottom_left.png").convert()
        self.bottom_left.set_colorkey((0, 0, 0))

        # decor images
        self.tree = pygame.image.load("data/sprites/decor/tree.png").convert()
        self.tree.set_colorkey((0, 0, 0))

        self.fence = pygame.image.load("data/sprites/decor/fence.png").convert()
        self.fence.set_colorkey((0, 0, 0))

        # coin images
        self.coin = pygame.image.load("data/sprites/coin/coin.png").convert()
        self.coin.set_colorkey((0, 0, 0))
    
    def render(self, surf):
        y = 0
        for row in self.tilemap:
            x = 0
            for collumn in row:
                if x * self.tile_size + self.tile_x > -self.tile_size and \
                        x * self.tile_size + self.tile_x < surf.get_width() and \
                        y * self.tile_size + self.tile_y > -self.tile_size and \
                        y * self.tile_size + self.tile_y < surf.get_height() + self.tile_size:
                    if collumn == '1':
                        surf.blit(self.grass_mid, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '2':
                        surf.blit(self.grass_right, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '3':
                        surf.blit(self.grass_left, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '4':
                        surf.blit(self.dirt_mid, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '5':
                        surf.blit(self.dirt_right, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '6':
                        surf.blit(self.dirt_left, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '7':
                        surf.blit(self.bottom_mid, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '8':
                        surf.blit(self.bottom_right, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '9':
                        surf.blit(self.bottom_left, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '10':
                        surf.blit(self.tree, (x * self.tile_size + self.tile_x, y * self.tile_size + 1 + self.tile_y))
                    elif collumn == '11':
                        surf.blit(self.fence, (x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y))
                    elif collumn == '12':
                        surf.blit(self.coin, ((x * self.tile_size + self.tile_x) / self.coin.get_width(), y * self.tile_size + self.tile_y))
                x += 1
            y += 1
    
    def create_collisions(self, surf):
        self.tilemap_collisions = []
        y = 0
        for row in self.tilemap:
            x = 0
            for collumn in row:
                if x * self.tile_size + self.tile_x > -self.tile_size and \
                        x * self.tile_size + self.tile_x < surf.get_width() and \
                        y * self.tile_size + self.tile_y > -self.tile_size and \
                        y * self.tile_size + self.tile_y < surf.get_height() + self.tile_size:
                    if not collumn == '0' and not collumn == '12':
                        self.tilemap_collisions.append(pygame.Rect(x * self.tile_size + self.tile_x, y * self.tile_size + self.tile_y, self.tile_size, self.tile_size))
                    elif collumn == '12':
                        self.tilemap_collisions.append(pygame.Rect((x * self.tile_size + self.tile_x) + (self.coin.get_width() / 2), (y * self.tile_size + self.tile_y) + (self.coin.get_height() / 2), self.tile_size, self.tile_size))
                x += 1
            y += 1

    def movement(self, tilemap_collisions):
        for tile in self.tilemap_collisions:
            tilemap_collisions.remove(tile)
        self.create_collisions()
        for tile in self.tilemap_collisions:
            tilemap_collisions.append(tile)