import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for program 'name_function.py'."""

    def test_first_last_name(self):
        """Is data 'Janis Joplin' supported?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_name(self):
        """Is data 'Wolfgang Amadeus Mozart' supported?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()
