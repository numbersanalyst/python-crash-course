import sys

import pygame

from random import randint

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from star import Star


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
        self.stars = pygame.sprite.Group()
        self._create_stars(3)

    def run(self):
        """Main game loop."""
        while True:
            self._update_screen()
            self._check_for_events()
            self.rocket.update_position()
            self._update_bullets_position()
            self._star_update()

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
        if len(self.bullets.sprites()) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets_position(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _create_stars(self, number_of_stars):
        for _ in range(number_of_stars):
            star = Star(self)
            self.stars.add(star)

    def _check_star_bullet_collision(self):
        collision = pygame.sprite.groupcollide(
            self.stars, self.bullets, True, True)

        if not self.stars:
            self._create_stars(randint(1, 5))

    def _star_update(self):
        self._check_star_bullet_collision()
        self.stars.update()

    def _update_screen(self):
        """Update the objects on the screen and move to the new screen."""
        self.screen.fill(self.settings.screen_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sr = ShootingRocket()
    sr.run()
