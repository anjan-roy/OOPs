class Student:
    def __init__(self, name, age):
        self.name = name        # Instance variable
        self.age = age          # Instance variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Alice", 21)
s1.display()
