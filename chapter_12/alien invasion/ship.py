import pygame

class Ship:
    """Class designed to control the spaceship."""

    def __init__(self, ai_game):
        """Initialize the spaceship and its launch position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship will appear on the bottom screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display the spaceship at its actual position."""
        self.screen.blit(self.image, self.rect)