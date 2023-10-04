import sys

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet


class ShootingRocket:
    """Class representing the game with the shooting rocket."""

    def __init__(self):
        """Initialize the game window and base data."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Shooting Rocket')

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def run(self):
        """Main game loop."""
        while True:
            self._update_screen()
            self._check_for_events()
            self.rocket.update_position()
            self._update_bullets_position()

    def _check_for_events(self):
        """Reacts to events inside the game."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reacts to keydown events."""
        if event.key == pygame.K_UP:
            self.rocket.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reacts to keyup events."""
        if event.key == pygame.K_UP:
            self.rocket.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_bottom = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets_position(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update the objects on the screen and move to new screen."""
        self.screen.fill(self.settings.screen_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        pygame.display.flip()


if __name__ == '__main__':
    sr = ShootingRocket()
    sr.run()
