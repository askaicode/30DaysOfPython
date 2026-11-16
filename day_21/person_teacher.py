class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old.'

    def birthday(self):
        self.age += 1


class Teacher(Person):
    def __init__(self, firstname, lastname, age, subject):
        super().__init__(firstname, lastname, age)
        self.subject = subject

    def person_info(self):
        return f'{super().person_info()} Teaches {self.subject}.'


p = Person('askaicode', 'lastname', 24)
print(p.age)
p.birthday()
print(p.age)
p.birthday()
print(p.age)
print(p.person_info())

t = Teacher('Lidiya', 'Teklemariam', 28, 'Math')
print(t.person_info())
t.birthday()
print(t.age)