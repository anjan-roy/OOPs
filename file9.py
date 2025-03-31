#concept of destructor
class test:
    def __init__(self):
        print('constructor')
    def __del__(self):
        print('destructor')
t=test()
t2=t
t3=t
del t
del t2
del t3
print('end of excution')