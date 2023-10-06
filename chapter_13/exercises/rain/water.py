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
        """Check if the water drop has reached the bottom of the screen."""
        if self.rect.top > self.screen_rect.bottom:
            return True
        return False

    def update(self):
        """Update the position of the water drop (falling)."""
        self.rect.y += 1
