from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_type(self):
        return "Unknown"

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

    def fuel_type(self):
        return "Petrol"

# Usage
c = Car()
print(c.start_engine())
print(c.fuel_type())
