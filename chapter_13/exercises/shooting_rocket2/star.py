import pygame

from random import randint


class Star(pygame.sprite.Sprite):
    """Class representing a star object."""

    def __init__(self, game):
        super().__init__()

        self.settings = game.settings

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        screen_width, screen_height = game.screen.get_size()

        self.rect.x = screen_width - self.rect.width
        self.rect.y = randint(0, screen_height-self.rect.height)

        self.x = float(self.rect.x)

    def update(self):
        """Change the position of the star."""
        self.x -= self.settings.star_speed
        self.rect.x = self.x
