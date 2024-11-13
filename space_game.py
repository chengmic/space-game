import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class SpaceBattle:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Battle")
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((700,700))

        # use these for fullscreen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            
            elif event.type ==pygame.KEYUP:
                self._check_keyup(event)
                    
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = True

        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.is_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.is_moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            #create new bullet
            new_bullet = Bullet(self)
            # add new bullet to bullets group
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.top <=0:
                self.bullets.remove(bullet)
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        curr_x = alien_width

        while curr_x < (self.settings.screen_width -(1 * alien_width)):
            self._create_alien(curr_x)
            curr_x += (2 * alien_width)

    def _create_alien(self, x_pos):
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        self.aliens.add(new_alien)

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            self.aliens.draw(self.screen)
            
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()


            # make most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make game instance and run game
    ai = SpaceBattle()
    ai.run_game()

