import pygame


class Ship:
    """A class representing a moving ship object."""

    def __init__(self, game):
        """Initialize the ship."""
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.set_position()

        self.moving_top = False
        self.moving_bottom = False

        self.y = float(self.rect.y)

    def set_position(self):
        """Set the ship on the center left of the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = self.rect.y # update y postion

    def update_position(self):
        """Update the position of the ship."""
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.s_speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.s_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship on the screen."""
        self.screen.blit(self.image, self.rect)