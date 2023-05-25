# pylint: disable=R0903

class Summation:
    """
    This class contains methods to perform arithmetic operations. As of now, it supports only 
    the addition of two numbers through the `add_numbers` method.
    """

    def __init__(self):
        """Initialize Summation class."""
        pass

    @staticmethod
    def add_numbers(num1, num2):
        """
        This method takes two arguments (num1 and num2) and returns their sum. If one or both of 
        the arguments are not numbers (either integers or floats), it raises a ValueError with an 
        appropriate message.
        
        Parameters:
        num1 (int, float): The first number.
        num2 (int, float): The second number.

        Returns:
        int or float: The sum of num1 and num2.
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Both arguments must be of type int or float.")
        return num1 + num2
