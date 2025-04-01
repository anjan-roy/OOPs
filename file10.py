#HAS-A relationship
class mouse:
    def mouseInfo(self):
        print('Mouse specific functionality')
class laptop:
    def __init__(self):
        self.m=mouse()
        self.m.mouseInfo()
l=laptop()