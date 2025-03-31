#code to get no of object creayed
class test:
    count=0 #static variable
    def __init__(self):
        test.count+=1
    @classmethod
    def objectCount(cls):
        print(f'Number of object created is: {cls.count}')
t1=test()
t2=test()
t3=test()
test.objectCount()