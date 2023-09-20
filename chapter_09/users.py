class User():
    """A class representing an user."""

    def __init__(self, first_name, last_name, nickname, age):
        """User constructor."""
        self.f_name = first_name
        self.l_name = last_name
        self.nick = nickname
        self.age = age

    def describe_user(self):
        """Display information about user."""
        print(f'\n{self.f_name} {self.l_name}')
        print(f'Nickname: {self.nick}')
        print(f'Age: {self.age}')

    def greet_user(self):
        """Display a greeting message for the user."""
        msg = f'Nice to see you {self.f_name} {self.l_name}!'
        print(f'\n{msg}')

user1 = User('Krzysztof', 'Wąs', 'Kristopher', 45)
user2 = User('Peter', 'White', 'piterlemon', 24)
user3 = User('Claudia', 'John', 'SuperPower', 28)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()