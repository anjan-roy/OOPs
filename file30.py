from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # encapsulation

    @abstractmethod
    def calculate_bonus(self):
        pass

    def get_salary(self):
        return self.__salary

class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.10

class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.20
