
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
    @property                   # Так НЕ работает!!!
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
print(s)


# Вывод

# Traceback (most recent call last):
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 30, in <module>
#     s = SubPerson('Guido')
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 4, in __init__
#     self.name = name
# AttributeError: can't set attribute