''' 5. Abstraction '''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print('Bike is starting...')

bike = Bike()
bike.start()