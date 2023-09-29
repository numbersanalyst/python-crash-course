class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A class representing a car battery."""
    
    def __init__(self, size=75):
        """Batery constuructor"""
        self.size = size
        
    def describe(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.size}-kWh battery.")
        
    def upgrade(self):
        """Upgrading battery size and displays information about it."""
        if self.size != 100:
            self.size = 100
            print(f'Battery is upgraded to {self.size} KWh')
        else:
            print('You have already upraded battery!')
            
    def get_range(self):
        """Display information about car's available range."""
        if self.size == 75:
            range = 250
        elif self.size == 100:
            range = 320
        print(f'The car can travel {range} miles on full charge.')

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe()
my_tesla.battery.upgrade()
my_tesla.battery.get_range()