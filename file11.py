class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrew {amount}. New balance: {self.balance}"

class Bank:
    def __init__(self, bank_name, account):
        self.bank_name = bank_name
        self.account = account  # HAS-A relationship

    def get_account_info(self):
        return f"Bank: {self.bank_name}, Account No: {self.account.account_number}, Balance: {self.account.balance}"

# Creating an Account object
acc1 = Account("123456", 5000)

# Creating a Bank object with an Account instance
bank1 = Bank("Python Bank", acc1)

# Testing
print(bank1.get_account_info())  # Output: Bank: Python Bank, Account No: 123456, Balance: 5000
print(bank1.account.deposit(2000))  # Deposit money
print(bank1.account.withdraw(3000))  # Withdraw money
print(bank1.account.withdraw(5000))  # Insufficient funds case
