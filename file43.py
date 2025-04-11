class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return "Area = length * breadth"

class Circle(Shape):
    def area(self):
        return "Area = π * r^2"

# Polymorphism in action
shapes = [Rectangle(), Circle()]
for shape in shapes:
    print(shape.area())
