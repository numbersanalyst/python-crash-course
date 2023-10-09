import sys

import pygame

from time import sleep

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from rect import Rect
from bullet import Bullet


class Game:
    """Game with ship and rect."""

    def __init__(self):
        """Initialize the game window, and base data."""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode(
            (self.settings.w_width, self.settings.w_height))
        pygame.display.set_caption('Ship and Rect')

        self.ship = Ship(self)
        self.rect = Rect(self)
        self.bullets = pygame.sprite.Group()
        self.button = Button(self, 'Play')

    def run(self):
        """Main program loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update_position()
                self.rect.update_position()
                self.bullets.update()

                self._check_bullet_rect_collision()

            self._screen_update()

    def _check_events(self):
        """Check if events are invoked."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_btn(mouse_pos)

    def _check_keydown_events(self, event):
        """Check if the key is pressed."""
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire()

    def _check_keyup_events(self, event):
        """Check if the key is not pressed."""
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _game_stop(self):
        self.stats.game_active = False
        pygame.mouse.set_visible(True)
        if self.button.text == 'Play':
            self.button = Button(self, 'Play again')

    def _start_game(self):
        """Start and reset the game."""
        if not self.stats.game_active:
            self.stats.game_active = True
            pygame.mouse.set_visible(False)
            self.bullets.empty()
            self.ship.set_position()
            self.rect.set_position()
            self.stats.reset()
            sleep(0.3)

    def _check_play_btn(self, mouse_pos):
        """If play button is pressed that stars the game."""
        if self.button.rect.collidepoint(mouse_pos):
            self._start_game()

    def _fire(self):
        """Fire the bullet."""
        if self.stats.bullets_left > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.stats.bullets_left -= 1
        else:
            self._game_stop()

    def _check_bullet_rect_collision(self):
        """Collect the collision between the bullet and reactangle."""
        if pygame.sprite.spritecollideany(self.rect, self.bullets):
            self._rect_hit()

    def _rect_hit(self):
        """Reaction to hit a moving rectangle."""
        sleep(0.5)
        self._game_stop()

    def _screen_update(self):
        """Update the screen and objects."""
        self.screen.fill(self.settings.background)
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.blitme()
        self.rect.draw()
        if not self.stats.game_active:
            self.button.draw()

        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()
