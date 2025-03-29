#excample of instance method
#OOPS concept
class employee:
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    def empinfo(self):
        print(f'Employee name:{self.name}')
        print(f'Employee id:{self.empid}')
        print(f'Employee salary:{self.salary}')
n=int(input('enter no of employee:'))
for i in range(0,n):
    name=input('Enter employee name:')
    empid=int(input('Enter employee id'))
    salary = int(input('Enter employee salary'))
    e=employee(name,empid,salary)
    e.empinfo()
    option=input('Do you want to insert more employee data?[yes/no]')
    if option.lower()=='no':
        break

