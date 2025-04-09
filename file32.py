# oops_loophole_1_mutable_default_args.py

class Bag:
    def __init__(self, items=[]):
        self.items = items

    def add(self, item):
        self.items.append(item)

    def show(self):
        print(self.items)

bag1 = Bag()
bag1.add('apple')

bag2 = Bag()
bag2.add('banana')

# Both bags share the same list!
bag1.show()  # ['apple', 'banana']
bag2.show()  # ['apple', 'banana']
