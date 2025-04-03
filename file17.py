class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  # Car has an Engine (Aggregation)

    def start_car(self):
        self.engine.start()
        print("Car is running")

engine = Engine()
car = Car(engine)
car.start_car()
