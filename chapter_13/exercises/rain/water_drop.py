import sys
import pygame

from water import Water


class Game:
    """A window with water."""

    def __init__(self):
        """Initialize the game window and create the rain."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Water drop!')

        self.drops_water = pygame.sprite.Group()
        self._create_rain()

    def run(self):
        """Main game loop that handles game events and updates the display."""
        while True:
            self._update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_rain(self):
        """Create a rain of water drops on the screen."""
        water = Water(self)  # for example

        available_space_x = self.screen.get_width()
        available_space_y = self.screen.get_height()

        number_waters = available_space_x // (2*water.rect.width)
        number_rows = available_space_y // (2*water.rect.height)

        for number_row in range(number_rows):
            for number_water in range(number_waters):
                self._create_water(number_water, number_row)

    def _create_water(self, number_water, number_row):
        """Create a water drop and position it on the screen."""
        water = Water(self)
        water.rect.x = number_water * 2 * water.rect.width
        water.rect.y = number_row * 3 * water.rect.height
        self.drops_water.add(water)

    def _rain_destroy(self):
        """Remove water drops that have reached the edge of the screen."""
        for water in self.drops_water.sprites():
            if water.check_for_edge():
                self.drops_water.remove(water)

    def _rain_create_new(self):
        """Recreate the rain when there are no water drops left."""
        if len(self.drops_water) == 0:
            self._create_rain()

    def _rain_managment(self):
        """Manage the behavior of the rain, including updates and recreation."""
        self.drops_water.update()
        self._rain_destroy()
        self._rain_create_new()
        self.drops_water.draw(self.screen)

    def _update(self):
        """Update the game screen and manage the rain in the main loop."""
        self.screen.fill((255, 255, 255))
        self._rain_managment()
        pygame.display.flip()


if __name__ == '__main__':
    stars = Game()
    stars.run()
