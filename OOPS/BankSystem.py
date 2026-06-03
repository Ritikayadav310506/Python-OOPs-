class BankAccount:
    def __init__(self, balance=0):   # constructor with default balance
        self.__balance = balance     # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


# Example 
account = BankAccount(1000)   # initial balance
account.deposit(500)          # deposit money
account.withdraw(200)         # withdraw money
print("Current Balance:", account.get_balance())
