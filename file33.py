# oops_loophole_2_name_mangling.py

class Secret:
    def __init__(self):
        self.__hidden = "Can't touch this!"

    def reveal(self):
        print(self.__hidden)

s = Secret()
# print(s.__hidden)  # AttributeError
print(s._Secret__hidden)  # Bypasses name mangling
