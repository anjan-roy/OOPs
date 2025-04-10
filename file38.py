class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):  # Multiple Inheritance
    pass

d = D()
d.show()  # Output: B's show (Python uses MRO - Method Resolution Order)
