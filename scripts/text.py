import pygame

class Text:
    def __init__(self, text, font, text_color, x, y):
        self.text = text
        self.font = font

        self.text_color = text_color

        self.x = x
        self.y = y

    def draw_text(self, surf):
        self.img = self.font.render(self.text, True, self.text_color)
        surf.blit(self.img, (self.x, self.y))