import pygame

from scripts import physics_entity

class Player(physics_entity.PhysicsEntity):
    def __init__(self, x, y, speed, jump_height, gravity, max_velocity, image):
        
        physics_entity.PhysicsEntity.__init__(self, x, y, image, max_velocity)
        
        self.speed = speed
        
        self.moving_right = False
        self.moving_left = False
        self.x_velocity = 0

        self.y_velocity = 0
        self.on_ground = False
        self.jumping = False
        self.jump_height = jump_height
        self.gravity = gravity

    def movement(self):
        self.x_velocity = (self.moving_right - self.moving_left) * self.speed

        if self.jumping == True and self.on_ground == True:
            self.y_velocity = -self.jump_height
            self.on_ground = False
        else:
            self.y_velocity += self.gravity
            if self.y_velocity > self.max_velocity:
                self.y_velocity = self.max_velocity

    