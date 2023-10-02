import unittest
from city_functions import get_city_country_name

class CitiesNamesTest(unittest.TestCase):
    """Test of the 'city_functions.py' program."""

    def test_city_country(self):
        """Are the country 'Chille' and city 'Santiago' supported?"""
        formatted_name = get_city_country_name('Santiago','Chille')
        self.assertEqual(formatted_name, 'Santiago, Chille')

    def test_city_country_population(self):
        """Are the country 'Chille' and city 'Santiago' with 5000000 population supported?"""
        formatted_name = get_city_country_name('Santiago','Chille', 5_000_000)
        self.assertEqual(formatted_name, 'Santiago, Chille - 5000000 population')

if __name__ == '__main__':
    unittest.main()