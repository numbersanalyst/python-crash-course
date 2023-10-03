import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """A general class designed to manage resources and how the game works."""

    def __init__(self):
        """Initialize the game and create their resorces."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Run the main game loop."""
        while True:
            # Waiting for click mouse or press key on keyboard.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refresh the screen every loop iteration.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Show the last modified screen.
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
