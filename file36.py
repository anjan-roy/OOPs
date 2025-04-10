class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the parent method
        print("Dog barks")

dog = Dog()
dog.speak()  # Output: Dog barks
