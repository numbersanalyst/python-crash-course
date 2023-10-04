import sys

import pygame


class TestEvent:
    """A class representing blank window that captures and print keydown events."""

    def __init__(self):
        """Initialize the window."""
        pygame.init()
        pygame.display.set_mode((200, 100))
        pygame.display.set_caption('Test Pygame Events')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                    print(f'Info about event: {vars(event)}')


if __name__ == '__main__':
    test_app = TestEvent()
    test_app.run()
