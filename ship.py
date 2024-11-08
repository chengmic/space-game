import pygame

class Ship:
    def __init__(self, space_game):
        self.screen = space_game.screen
        self.settings = space_game.settings
        self.screen_rect = space_game.screen.get_rect()

        # load ship and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start ship at bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # ships x position
        self.x = float(self.rect.x)

        # movement
        self.is_moving_right = False
        self.is_moving_left = False

        

    def update(self):
        if self.is_moving_right:
            if self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed

        if self.is_moving_left:
            if self.rect.left > 0:
                self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw ship at current location"""
        self.screen.blit(self.image, self.rect)

