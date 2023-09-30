class Privilages():
    """Class representing a list of user privilages."""

    def __init__(self, privilages=['post', 'delete_post', 'ban', 'mute']):
        """Privilages constructor."""
        self.privilages = privilages

    def show_privilages(self):
        """Show the list of user privilages."""
        print(f'\nList of that user privilages:')
        for privilage in self.privilages:
            print(f'- {privilage}')
