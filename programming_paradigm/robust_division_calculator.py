# Robust Division Calculator with Command Line Arguments
import sys
def safe_divide(numerator, denominator):
    """
    Perform division and handle exceptions.
    
    Args:
        numerator (float): The number to be divided.
        denominator (float): The number by which to divide.
    
    Returns:
        float: The result of the division or an error message.
    """
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return f"Result: {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please provide numeric values for division."
    except ValueError:
        return "Error: Please enter numeric values only."