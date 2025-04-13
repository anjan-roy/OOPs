class Calculator:
    def add(self, a, b):
        result = a + b       # Local variable
        print("Addition:", result)

calc = Calculator()
calc.add(10, 20)
