''' Encapsulation '''
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private Attribute
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposited {amount}. New Balance: {self.__balance}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawn {amount}. New Balance: {self.__balance}')
        else:
            print('Insufficient funds!')

    def get_balance(self):
        return self.__balance

account = BankAccount(12345, 5000)
account.deposit(1000)
account.withdraw(2000)
print(f'Current Balance: {account.get_balance()}')