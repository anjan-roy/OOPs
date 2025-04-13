class MathUtils:
    @staticmethod
    def multiply(x, y):
        result = x * y       # Local variable in static method
        print("Multiplication:", result)

MathUtils.multiply(5, 4)
