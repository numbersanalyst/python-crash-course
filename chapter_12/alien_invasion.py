import sys

import pygame


class AlienInvasion:
    """A general class designed to manage resources and how the game works."""

    def __init__(self):
        """Initialize the game and create their resorces."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Run the main game loop."""
        while True:
            # Waiting for click mouse or press key on keyboard.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show the last modified screen.
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()