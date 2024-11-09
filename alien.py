import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, space_game):
        super().__init__()
        self.screen = space_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's exact horizontal pos
        self.x = float(self.rect.x)
