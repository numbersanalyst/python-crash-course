import pygame


class Star(pygame.sprite.Sprite):
    """Class representing a star object."""

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height