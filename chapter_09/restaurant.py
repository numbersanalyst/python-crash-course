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


restaurant = Restaurant('American Burgers&Steaks', 'Fast food')

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()
