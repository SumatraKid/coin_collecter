import pygame

import sys

from scripts import player, tilemap, physics_entity, text

class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.Clock()
        self.fps = 60

        self.screen = pygame.display.set_mode((750, 750), 0, 32)
        self.display = pygame.Surface((350, 350), 0, 32)

        self.start()

        # game loop
        self.running = True
        while self.running == True:

            # input
            self.input()

            # logic
            self.update()

            # rendering
            self.draw()
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            pygame.display.flip()
            self.clock.tick(self.fps)
            

        # quits the game
        pygame.quit()
        sys.exit()
    

    # starts once in the begining
    def start(self):
        self.player = player.Player(100, 100, 2, 6, 0.4, 10, "data/sprites/player/player_idle_right.png")

        self.score = 0
        self.score_font = pygame.font.SysFont("Ariel", 50)
        self.score_text = text.Text(str(self.score), self.score_font, (0, 0, 0), 300, 10)


        self.scene = "one"

        self.tilemap_coins = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_coins.txt")
        self.tilemap_coins.create_collisions(self.display)
        self.coin_image = pygame.image.load("data/sprites/coin/coin.png").convert()
        self.coin_image.set_colorkey((0, 0, 0))

        self.tilemap_decor = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_decor.txt")
        self.tilemap_1 = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_layer_1.txt")
        self.tilemap_2 = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_layer_2.txt")

        self.tilemap_1.create_collisions(self.display)
        self.tilemap_2.create_collisions(self.display)

        self.tilemap_collisions = []
        for tile in self.tilemap_1.tilemap_collisions:
            self.tilemap_collisions.append(tile)
        for tile in self.tilemap_2.tilemap_collisions:
            self.tilemap_collisions.append(tile)

    # game input
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                if event.key == pygame.K_UP:
                    self.player.jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                if event.key == pygame.K_UP:
                    self.player.jumping = False
                if event.key == pygame.K_e:
                    fps = self.clock.get_fps()
                    print(f"Current FPS: {fps:.2f}")
                if event.key == pygame.K_q:
                    self.scene = "two"

                    self.tilemap_coins = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_coins.txt")
                    self.tilemap_coins.create_collisions(self.display)
                    self.coin_image = pygame.image.load("data/sprites/coin/coin.png").convert()
                    self.coin_image.set_colorkey((0, 0, 0))

                    self.tilemap_decor = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_decor.txt")
                    self.tilemap_1 = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_layer_1.txt")
                    self.tilemap_2 = tilemap.Tilemap(32, 0, 0, "data/scene_" + self.scene + "/tilemap_layer_2.txt")
                    self.tilemap_1.create_collisions(self.display)
                    self.tilemap_2.create_collisions(self.display)

                    self.tilemap_collisions = []
                    for tile in self.tilemap_1.tilemap_collisions:
                        self.tilemap_collisions.append(tile)
                    for tile in self.tilemap_2.tilemap_collisions:
                        self.tilemap_collisions.append(tile)
                    

    # game logic
    def update(self):

        self.score_text.text = str(self.score)

        # player movement and collisions
        self.player.movement()
        self.player.x += self.player.x_velocity
        self.player.collider.x = self.player.x

        collisions = self.player.collision_test(self.tilemap_collisions)
        for tile in collisions:
            if self.player.x_velocity > 0:
                self.player.x = tile.x - self.player.image.get_width()
            if self.player.x_velocity < 0:
                self.player.x = tile.x + tile.width
                self.player.x_velocity = 0
        self.player.collider.x = self.player.x

        self.player.y += self.player.y_velocity
        self.player.collider.y = self.player.y

        if self.player.y_velocity > 2:
            self.player.on_ground = False

        collisions = self.player.collision_test(self.tilemap_collisions)
        for tile in collisions:
            if self.player.y_velocity > 0:
                self.player.y = tile.y - self.player.image.get_height()
                self.player.y_velocity = 0
                self.player.on_ground = True
            if self.player.y_velocity < 0:
                self.player.y = tile.y + tile.height
                self.player.y_velocity = 0
        self.player.collider.y = self.player.y

        # coin collisions
        for coin in self.tilemap_coins.tilemap_collisions:
            if coin.colliderect(self.player.collider):
                self.score += 1
                self.tilemap_coins.tilemap_collisions.remove(coin)
                del coin
        

    # game rendering
    def draw(self):
        self.display.fill((52.0, 133.0, 157.0))

        self.tilemap_decor.render(self.display)
        self.tilemap_2.render(self.display)
        self.tilemap_1.render(self.display)

        self.score_text.draw_text(self.display)

        for coin in self.tilemap_coins.tilemap_collisions:
            self.display.blit(self.coin_image, (coin.x, coin.y))

        self.display.blit(self.player.image, (self.player.x, self.player.y))

Game()