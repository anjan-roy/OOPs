class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):
        print("This is the Child class method.")
        super().show()  # Call the parent class method

# Create an object of Child
c = Child()
c.show()
