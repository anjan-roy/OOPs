class A:
    def greet(self):
        print("Hello from Class A")

class B(A):
    def greet(self):
        print("Hello from Class B")
        super().greet()  # Call greet() from class A

class C(B):
    def greet(self):
        print("Hello from Class C")
        super().greet()  # Call greet() from class B

# Create an object of class C
obj = C()
obj.greet()
