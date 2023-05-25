"""
This module contains the TestSum class which uses Python's built-in `unittest` module to test 
the `add_numbers` method in the `Summation` class.
"""
import unittest
from sum import Summation

class TestSum(unittest.TestCase):
    """
    This class contains methods to perform arithmetic operations. As of now, it supports only 
    the addition of two numbers through the `add_numbers` method.
    """
    def test_add_numbers(self):
        """
        This test checks that the add_numbers method returns the correct sum of two numbers.
        """
        self.assertEqual(Summation.add_numbers(1, 2), 3)
        self.assertAlmostEqual(Summation.add_numbers(1.1, 2.2), 3.3, places=2)

    def test_add_numbers_error(self):
        """
        This test ensures that the add_numbers method raises a ValueError if a string is passed as an argument.
        """
        with self.assertRaises(ValueError):
            Summation.add_numbers("one", 2)

if __name__ == '__main__':
    """
    If the script is run directly (rather than imported), this code is executed. It runs all the tests 
    in the TestSum class. If the tests pass, it will print out a message saying so. If any test fails, 
    it will print out an error message detailing what went wrong.
    """
    unittest.main()
