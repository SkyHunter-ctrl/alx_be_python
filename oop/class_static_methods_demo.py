# Distinguishing Between Class Methods and Static Methods
# Class methods are bound to the class and not the instance.
# They can modify class state that applies across all instances of the class.
# Static methods do not modify class or instance state and are utility functions.
class Calculator:
    # class attribute
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of x and y."""
        return a + b
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Returns the product of x and y."""
        print(f"Calculation type: {cls.calculation_type}")  
        return a * b
# Example usage
def main():
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
if __name__ == "__main__":
    main()
    