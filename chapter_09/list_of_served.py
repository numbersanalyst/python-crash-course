class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Restaurant constructor."""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.served = number_served

    def describe_restaurant(self):
        """Display the information about a restaurant."""
        print(f'Restaurant name: {self.name}')
        print(f'Cuisine type: {self.cuisine}')
        print(f'Number of people served: {self.served}')

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        print(f'Restaurant {self.name} is open, come on!')

    def set_number_served(self, number):
        """Set the number of served users."""
        self.served = number

    def increment_number_served(self, number):
        """Increment the number of served users."""
        self.served += number
