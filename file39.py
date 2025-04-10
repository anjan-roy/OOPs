class Employee:
    def work(self):
        print("Employee works 9 to 5")

class Manager(Employee):
    def work(self):
        super().work()
        print("Manager also attends meetings")

m = Manager()
m.work()
