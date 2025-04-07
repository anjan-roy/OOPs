class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent class constructor
        self.breed = breed
        print(f"Dog created: {self.name}, Breed: {self.breed}")

# Create an object of Dog
d = Dog("Rocky", "Labrador")
