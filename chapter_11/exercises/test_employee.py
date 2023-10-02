import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests employee class."""

    def setUp(self):
        """Creates a new employee to use in all test methods."""
        self.employee = Employee('John','Johnson', 48_000)

    def test_give_default_raise(self):
        """Checks that the employee rewards default raises."""
        new_salary = self.employee.salary + 5_000
        self.employee.give_rise()
        self.assertEqual(new_salary, self.employee.salary)

    def test_give_custom_raise(self):
        """Checks that the employee rewards custom raises."""
        new_salary = self.employee.salary + 7_000
        self.employee.give_rise(7_000)
        self.assertEqual(new_salary, self.employee.salary)

if __name__ == '__main__':
    unittest.main()