import sys
import pygame

from water import Water


class Game:
    """A window with stars."""

    def __init__(self):
        """Initialize the basic window properties."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Stars')

        self.drops_water = pygame.sprite.Group()
        self._create_rain()

    def run(self):
        """Main game loop."""
        while True:
            self._update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _rain_destroy(self):
        for water in self.drops_water.sprites():
            if water.check_for_edge():
                self.drops_water.remove(water)

    def _rain_managment(self):
        self.drops_water.update()
        self._rain_destroy()
        self.drops_water.draw(self.screen)

    def _update(self):
        self.screen.fill((255, 255, 255))
        self._rain_managment()
        pygame.display.flip()

    def _create_rain(self):
        water = Water(self)  # for example

        available_space_x = self.screen.get_width()
        available_space_y = self.screen.get_height()

        number_waters = available_space_x // (2*water.rect.width)
        number_rows = available_space_y // (2*water.rect.height)

        for number_row in range(number_rows):
            for number_water in range(number_waters):
                self._create_water(number_water, number_row)

    def _create_water(self, number_water, number_row):
        water = Water(self)
        water.rect.x = number_water * 2 * water.rect.width
        water.rect.y = number_row * 3 * water.rect.height
        self.drops_water.add(water)


if __name__ == '__main__':
    stars = Game()
    stars.run()
