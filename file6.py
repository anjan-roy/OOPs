#nested method
class test:
    def m1(self):
        def sum(a,b):
            print(a+b)
        def sub(a,b):
            print(a-b)
        def mul(a,b):
            print(a*b)
        def div(a,b):
            if b==0:
                print('division not possible')
            else:
                print(a/b)
        sub(34,67)
        sub(54,31)
        mul(23,87)
        div(63,9)
test().m1()
