#bank application
class bank:
    bank_name='ABC India pvt ltd' #static variable
    def __init__(self,balance=0):
        self.balance=0
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+amount
        print(f'Current available balance is {self.balance}')
    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.balance-amount
        print(f'Current available balance is {self.balance}')
print(f'Welcome to {bank.bank_name}')
b=bank()
while True:
    option=int(input('Enter 1 for balance:\n Enter 2 to deposit money:\n Enter 3 to withdraw money:'))

    if option==1:
        print(f'Current available balance is {b.balance}')
    elif option==2:
        amount=float(input('enter amount:'))
        b.deposit(amount)
    elif option==3:
        amount=float(input('enter amount:'))
        b.withdraw(amount)
    else:
        break
