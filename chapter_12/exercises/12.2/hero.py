import pygame

class Hero:
    """Class representing a hero character."""

    def __init__(self, game):
        """Initialize the hero and its launch position."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/hero.bmp')
        self.img_rect = self.img.get_rect()

        self.img_rect.center = self.screen_rect.center

    def biltme(self):
        """Display the hero at its actual position."""
        self.screen.blit(self.img, self.img_rect)