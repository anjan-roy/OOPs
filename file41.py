class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Object of Dog class
d = Dog()
d.speak()  # Output: Dog barks
