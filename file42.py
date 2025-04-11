class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# Accessing through methods
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
