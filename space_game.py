import sys
import pygame
from settings import Settings

class SpaceBattle:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Battle")



    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #rewdraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            
            # make most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # make game instance and run game
    ai = SpaceBattle()
    ai.run_game()

