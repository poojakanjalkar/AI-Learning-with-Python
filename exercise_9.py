class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b

def main():
    calc = Calculator()

    print("Welcome to the Simple Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please restart the program.")
            return
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"The result of addition is: {calc.add(num1, num2)}")
        elif choice == 2:
            print(f"The result of subtraction is: {calc.subtract(num1, num2)}")
        elif choice == 3:
            print(f"The result of multiplication is: {calc.multiply(num1, num2)}")
        elif choice == 4:
            print(f"The result of division is: {calc.divide(num1, num2)}")
    except ValueError:
        print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    main()
