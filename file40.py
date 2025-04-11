class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Object creation
student1 = Student("Rahul", "A")
student1.display_info()
