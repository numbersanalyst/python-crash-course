import sys

import pygame

from settings import Settings
from ship import Ship
from rect import Rect
from bullet import Bullet

class Game:
    """Game with ship and rect."""

    def __init__(self):
        """Initialize the game window, and base data."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.w_width, self.settings.w_height))
        pygame.display.set_caption('Ship and Rect')

        self.ship = Ship(self)
        self.rect = Rect(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        """Main program loop."""
        while True:
            self._check_events()
            self.ship.update_position()
            self.rect.update_position()
            self.bullets.update()
            self._check_bullet_rect_collision()
            self._screen_update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _fire(self):
        if self.settings.s_ammo > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.settings.s_ammo -= 1
        else:
            print('koniec')

    def _check_bullet_rect_collision(self):
        if pygame.sprite.spritecollideany(self.rect, self.bullets):
            print('traf')

    def _screen_update(self):
        """Update the screen and objects."""
        self.screen.fill(self.settings.background)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        self.rect.draw()
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
