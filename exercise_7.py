class Calculator:
    def __init__(self):
        """Initialize the calculator with no values."""
        print("Calculator initialized!")

    def add(self, a, b):
        """Method to add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Method to subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Method to multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Method to divide two numbers."""
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


# Create an instance of the class
calc = Calculator()

# Perform operations
print("Addition:", calc.add(10, 5))         # Output: 15
print("Subtraction:", calc.subtract(10, 5)) # Output: 5
print("Multiplication:", calc.multiply(10, 5)) # Output: 50
print("Division:", calc.divide(10, 5))      # Output: 2.0
