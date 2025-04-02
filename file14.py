'''Polymorphism'''
class Bird:
    def fly(self):
        return 'Flying in the sky'

class Airplane:
    def fly(self):
        return 'Flying at high altitude'

objects = [Bird(), Airplane()]
for obj in objects:
    print(obj.fly())