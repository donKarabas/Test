
class Person:
    def __init__(self, name):
        self.name = name

    # Функция-геттер
    @property
    def name(self):
        return self._name

    # Функция-сеттер
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Функция-делитер
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
print(s)

print()

print(s.name)

print()

s.name = 'Larry'
print(s.name)

print()

s.name = 42
print(s)


# Вывод

# __main__.SubPerson object at 0x7fc0acc7efd0>
#
# Getting name
# Guido
#
# Getting name
# Larry
#
# Traceback (most recent call last):
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 44, in <module>
#     s.name = 42
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 15, in name
#     raise TypeError('Expected a string')
# TypeError: Expected a string
