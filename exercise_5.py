class NumberCheck:
    def __init__(self, number):
        self.number = number

    def check_even_odd(self):
        if self.number % 2 == 0:
            print(f"The number {self.number} is Even.")
        else:
            print(f"The number {self.number} is Odd.")

# Input from user
num = int(input("Enter a number: "))

# Create an object of the class and check even or odd
number_obj = NumberCheck(num)
number_obj.check_even_odd()
