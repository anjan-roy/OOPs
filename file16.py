class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine (Composition)

    def start_car(self):
        self.engine.start()
        print("Car is running")

car = Car()
car.start_car()
