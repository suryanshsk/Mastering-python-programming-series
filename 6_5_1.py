#bundling data and its methods into a 
# single unit, called a class
"""Encapsulation is the mechanism of restricting 
access to certain components of an object and only 
exposing a limited interface to the user."""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner         # Public attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Deposit amount must be positive."

    def get_balance(self):
        return f"Balance: {self.__balance}"

# Example Usage
account = BankAccount("Suryanshsk", 1000)
print(account.get_balance())  # Access balance safely
print(account.deposit(500))   # Add 500 to balance


# Trying to access private attribute directly (will fail)
# print(account.__balance)  # Uncommenting this will raise an AttributeError

