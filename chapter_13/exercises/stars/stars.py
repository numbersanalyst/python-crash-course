import sys
import pygame

from star import Star


class Game:
    """A window with stars."""

    def __init__(self):
        """Initialize the basic window properties."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Stars')

        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run(self):
        """Main game loop."""
        while True:
            self._update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update(self):
        self.screen.fill((255, 255, 255))
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _create_stars(self):
        star = Star()  # for example

        available_space_x = self.screen.get_width()
        available_space_y = self.screen.get_height()

        number_stars = available_space_x // (2*star.rect.width)
        number_rows = available_space_y // (2*star.rect.height)

        for number_row in range(number_rows):
            for number_star in range(number_stars):
                self._create_star(number_star, number_row)

    def _create_star(self, number_star, number_row):
        star = Star()
        star.rect.x = number_star * 2 * star.rect.width
        star.rect.y = number_row * 3 * star.rect.height
        self.stars.add(star)

if __name__ == '__main__':
    stars = Game()
    stars.run()
