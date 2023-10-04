import pygame


class Rocket:
    """Class designed to create and control the rocket."""
    def __init__(self, sr_game):
        """Initialize the rocket and its position."""
        self.screen = sr_game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = sr_game.settings

        self.img = pygame.image.load('images/rocket.bmp')
        self.rect = self.img.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_top = False
        self.moving_bottom = False

    def update_position(self):
        """Changes the position of the rocket."""
        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.y = self.y

    def blitme(self):
        """Display the rocket at the specified position."""
        self.screen.blit(self.img, self.rect)