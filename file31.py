from encapsulation_example import BankAccount
from abstraction_example import Car
from combined_concepts import Developer, Manager

# Encapsulation
print("=== Encapsulation Example ===")
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())

# Abstraction
print("\n=== Abstraction Example ===")
my_car = Car()
my_car.start_engine()
my_car.stop_engine()

# Combined
print("\n=== Combined Example ===")
dev = Developer("John", 50000)
mgr = Manager("Sara", 80000)
print(f"Developer Bonus: {dev.calculate_bonus()}")
print(f"Manager Bonus: {mgr.calculate_bonus()}")
