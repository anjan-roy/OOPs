# oops_loophole_3_dynamic_attribute_addition.py

class User:
    def __init__(self, name):
        self.name = name

u = User("Alice")
u.age = 25  # Dynamic attribute addition

print(u.name)  # Alice
print(u.age)   # 25

# But another instance doesn't have 'age'
v = User("Bob")
# print(v.age)  # AttributeError
