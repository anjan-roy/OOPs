#concept of destructor
class test:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('destructor')
t=test()
print('end of excution')