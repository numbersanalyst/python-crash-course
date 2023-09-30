from user_part import User
from privilages_part import Privilages

class Admin(User):
    """Class representing admin account."""

    def __init__(self, f_name, l_name, nick, age):
        """Admin account constructor."""
        super().__init__(f_name, l_name, nick, age)
        self.privilages = Privilages()
