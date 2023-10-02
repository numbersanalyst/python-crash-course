class Employee():
    """A class that represents a employee."""

    def __init__(self, f_name, l_name, salary):
        """Construct a new Employee profile."""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_rise(self, amount=5_000):
        """Gives rise to a employee."""
        self.salary += amount