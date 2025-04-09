# oops_loophole_4_inheritance_override_trap.py

class Base:
    def __init__(self):
        self.value = 10

    def print_value(self):
        print("Base value:", self.value)

class Child(Base):
    def __init__(self):
        # Forgot to call super().__init__()
        self.value = 42

c = Child()
c.print_value()  # Works fine

b = Base()
b.print_value()  # Works fine

# But if you rely on super(), things break silently in real apps
