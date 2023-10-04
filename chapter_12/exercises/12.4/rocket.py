import pygame


class Rocket:
    """Class representing a rocket."""

    def __init__(self, game):
        """Initialize the rocket and its launch position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/rocket.bmp')
        self.rect = self.img.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_top = False
        self.moving_bottom = False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position of the rocket."""
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def biltme(self):
        """Display the rocket at its actual position."""
        self.screen.blit(self.img, self.rect)
