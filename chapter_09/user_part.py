class User():
    """A class representing an user."""

    def __init__(self, first_name, last_name, nickname, age):
        """User constructor."""
        self.f_name = first_name.title()
        self.l_name = last_name.title()
        self.nick = nickname
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Display information about user."""
        print(f'\n{self.f_name} {self.l_name}')
        print(f'Nickname: {self.nick}')
        print(f'Age: {self.age}')

    def greet_user(self):
        """Display a greeting message for the user."""
        msg = f'Nice to see you {self.f_name} {self.l_name}!'
        print(f'\n{msg}')

    def inceremnt_login(self):
        """Increment the login counter."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempt counter."""
        self.login_attempts = 0
