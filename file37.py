class Father:
    def skills(self):
        print("Father: Gardening and Painting")

class Mother:
    def skills(self):
        print("Mother: Cooking and Dancing")

class Child(Father, Mother):
    def skills(self):
        print("Child: ", end="")
        Father.skills(self)
        Mother.skills(self)

child = Child()
child.skills()
