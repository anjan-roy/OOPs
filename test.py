#how to define a class and create object
class test:
    def __init__(self):
        self.name='Ran'
        self.address='Ayodhya'
    def info(self):
        print(self.name)
        print(self.address)
#creation of object
t=test()
#calling instance method by using reference variable t
t.info()