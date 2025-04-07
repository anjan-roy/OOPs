class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car-specific start procedure.")
        super().start()  # Call the Vehicle's start method

# Create an object of Car
c = Car()
c.start()
