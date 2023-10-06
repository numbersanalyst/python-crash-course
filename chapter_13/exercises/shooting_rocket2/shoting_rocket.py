import sys

import pygame

from random import randint
from time import sleep

from settings import Settings
from game_stats import GameStats
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

        self.stats = GameStats(self)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._create_stars(3)

    def run(self):
        """Main game loop."""
        while True:
            self._check_for_events()
            if self.stats.game_active:
                self.rocket.update_position()
                self._update_bullets_position()
                self._star_update()
            self._update_screen()

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
        """Fire a bullet if the bullet limit is not reached."""
        if len(self.bullets.sprites()) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets_position(self):
        """Update the position of bullets and remove off-screen bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.screen.get_rect().right:
                self.bullets.remove(bullet)

    def _create_stars(self, number_of_stars):
        """Create a specified number of stars."""
        for _ in range(number_of_stars):
            star = Star(self)
            self.stars.add(star)

    def _check_star_bullet_collision(self):
        """Check for collisions between stars and bullets."""
        collision = pygame.sprite.groupcollide(
            self.stars, self.bullets, True, True)

        if not self.stars:
            self._create_stars(randint(1, 5))

    def _check_stars_left(self):
        """Check if the stars are in the left of the screen."""
        for star in self.stars.sprites():
            if star.rect.left <= 0:
                self._hit_rocket()

    def _hit_rocket(self):
        """Handle rocket being hit by stars."""
        if self.stats.rocket_lives > 0:
            self.stats.rocket_lives -= 1

            self.bullets.empty()
            self.stars.empty()

            self._create_stars(3)
            self.rocket._rocket_center()

            sleep(2)
        else:
            self.stats.game_active = False

    def _star_update(self):
        """Update the position of stars and handle collisions."""
        self._check_star_bullet_collision()
        self._check_stars_left()

        if pygame.sprite.spritecollideany(self.rocket, self.stars):
            self._hit_rocket()

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
