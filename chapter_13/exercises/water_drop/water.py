import pygame


class Water(pygame.sprite.Sprite):
    """Class representing a water object."""

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/water.bmp')
        self.rect = self.image.get_rect()

    def check_for_edge(self):
        if self.rect.top > self.screen_rect.bottom:
            return True

    def update(self):
        self.rect.y += 1
