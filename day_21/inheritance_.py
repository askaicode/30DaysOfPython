class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    
    def person_info(self):
        return f'{self.firstname} is {self.age} years old.'
        

class Student(Person):
    def __init__(self, firstname, lastname, age, school):
        super().__init__(firstname, lastname, age)
        self.school = school
    
    def person_info(self):
        return f'{super().person_info()} Studies at {self.school}.'

s = Student('askaicode', 'taletsy', 24, 'Harvard University')
print(s.firstname)
print(s.person_info())