
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
    @Person.name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)


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

# Setting name to Guido
# <__main__.SubPerson object at 0x7fa2cd0b2fd0>
#
# Guido
#
# Setting name to Larry
# Larry
#
# Setting name to 42
# Traceback (most recent call last):
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 44, in <module>
#     s.name = 42
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 27, in name
#     super(SubPerson, SubPerson).name.__set__(self, value)
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 15, in name
#     raise TypeError('Expected a string')
# TypeError: Expected a string
