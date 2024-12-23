class ATM:
    def __init__(self, initial_balance=0):
        """Initialize the ATM with a default balance."""
        self.balance = initial_balance

    def check_balance(self):
        """Display the current balance."""
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if amount > self.balance:
            print("Insufficient funds! Unable to withdraw.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def atm_menu(self):
        """Display the ATM menu and process user input."""
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.check_balance()
                elif choice == 2:
                    amount = float(input("Enter amount to deposit: ₹"))
                    self.deposit(amount)
                elif choice == 3:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    self.withdraw(amount)
                elif choice == 4:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")


my_atm = ATM(5000)


my_atm.atm_menu()
