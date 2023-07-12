
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
    @Person.getter          # И так не работает!!!
    def name(self):
        print('Getting name')
        return super().name


s = SubPerson('Guido')
print(s.name)

# Вывод

# Traceback (most recent call last):
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 23, in <module>
#     class SubPerson(Person):
#   File "/home/lazutchik/PycharmProjects/data_files/test00.py", line 24, in SubPerson
#     @Person.getter          # И так не работает!!!
# AttributeError: type object 'Person' has no attribute 'getter'



