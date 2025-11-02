import pygame

class PhysicsEntity:
    def __init__(self, x, y, image, max_velocity):

        self.x = x
        self.x_velocity = 0

        self.y = y
        self.y_velocity = 0

        self.max_velocity = max_velocity

        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))

        self.collider = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.destroyed = False

    def collision_test(self, tilemap):
        tiles = []
        for tile in tilemap:
            if self.collider.colliderect(tile):
                tiles.append(tile)
        return tiles

