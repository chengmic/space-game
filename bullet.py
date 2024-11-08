import pygame
from pygame.sprite import Sprite

# inherits from Sprite
class Bullet(Sprite):
    def __init__(self, space_game):
        super().__init__()
        self.screen = space_game.screen
        self.settings = space_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = space_game.ship.rect.midtop

        #store bullet pos as float
        self.y = float(self.rect.y)


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """move bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y