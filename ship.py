import pygame

class Ship:
    def __init__(self, space_game):
        """init ship and set starting position of ship"""
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()

        # load ship and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start ship at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)

