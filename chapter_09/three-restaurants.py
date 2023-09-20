class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Restaurant constructor."""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Display the information about a restaurant."""
        print(f'Restaurant name: {self.name}')
        print(f'Cuisine type: {self.cuisine}')

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f'Restaurant {self.name} is open, come on!')


restaurant1 = Restaurant('American Burgers&Steaks', 'Fast food')
restaurant2 = Restaurant('Cactus', 'Bistro')
restaurant3 = Restaurant('Pasibus', 'Fast Casual')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
