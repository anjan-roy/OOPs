class Employee:
    company = "TechCorp"     # Class variable

    def __init__(self, name):
        self.name = name     # Instance variable

    def show(self):
        print(f"Employee: {self.name}, Company: {Employee.company}")

e1 = Employee("John")
e2 = Employee("Lisa")
e1.show()
e2.show()
