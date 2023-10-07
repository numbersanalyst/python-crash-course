import pygame

from random import randint


class Rect:
    """Creates a Rect moving object."""

    def __init__(self, game):
        """Initializes a Rect object."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(
            0, 0, self.settings.r_width, self.settings.r_height)

        self.rect.x = self.screen_rect.width - self.rect.width
        self.rect.y = randint(0, self.screen_rect.height - self.rect.height)

        self.y = float(self.rect.y)

    def update_position(self):
        """Change the position of the rect."""
        self._check_position()
        self.y -= self.settings.r_speed
        self.rect.y = self.y

    def _check_position(self):
        """Prevent the rect from being outside the screen."""
        if self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            self.settings.r_speed *= -1

    def draw(self):
        """Draw the rect on the screen."""
        pygame.draw.rect(self.screen, self.settings.r_color, self.rect)
