class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. Current balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. Current balance: ₹{self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")


print("Welcome to Bank Account Management System!")
name = input("Enter the account holder's name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Display Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == 3:
        account.display_balance()
    elif choice == 4:
        print("Thank you for using our system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
