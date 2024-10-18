import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """Creating instances at once"""

        self.employee = Employee('alaa', 'hamdy', 70000)

    def test_default_raise(self):
        """Testing the default raise"""

        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 75000)

unittest.main()