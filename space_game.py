import sys
import pygame
from settings import Settings
from ship import Ship

class SpaceBattle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Battle")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            
            # make most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make game instance and run game
    ai = SpaceBattle()
    ai.run_game()

