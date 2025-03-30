#inner class
class outer:
    def __init__(self):
        print('outer class constructor')
    class inner:
        def __init__(self):
            print('inner class constructor')
        def m1(self):
            print('inner class instance method')
        class inner2:
            def __init__(self):
                print('inner 2 class instance method')
            @classmethod
            def m2(cls):
                print('inner 2 class class method')
outer().inner().m1()
outer().inner().inner2.m2()