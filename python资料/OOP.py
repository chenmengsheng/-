# OOP Object-Oriented Programming
#bug to be fixed
#IDE: Integrated Development Environments
#build-in data-type
#user-defined
class Person:
    def __int__(self, _name, _age):
        self.name = _name
        self.age = _age


class Student(Person):
    pass


jack = Person("Jack", 28)
tom = Person("Tom", 18)
jack.teach(tom)
