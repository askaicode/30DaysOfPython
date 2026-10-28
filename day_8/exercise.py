# Day 8: Dictionaries

# 1. Create an empty dictionary called dog
dog = {}  # or dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'chiwawa'
dog['color'] = 'white'
dog['breed'] = 'French Bulldog'
dog['legs'] = 4
dog['age'] = 1
print('dog : ', dog)

# 3. Create a student dictionary
student = {
    'first_name': 'askaicode',
    'last_name': 'taletsy',
    'gender': 'male',
    'age': 24,
    'marital_status': 'single',
    'skills': ['HTML', 'CSS', 'Javascript', 'React', 'Node', 'Python'],
    'country': 'Madagascar',
    'city': 'Antananarivo',
    'address': 'Antananarivo, Madagascar'
}

# 4. Get the length of the student dictionary
print('student dictionary length : ', len(student))  # 9

# 5. Get the value of skills and check the data type
print('Skills : ', student['skills'])
print('skills data type : ', type(student['skills']))  # <class 'list'>

# 6. Modify the skills values by adding one or two skills
student['skills'].extend(['Java', 'MySQL'])
print('updated skills : ', student['skills'])

# 7. Get the dictionary keys as a list
print('keys as a list : ', list(student.keys()))

# 8. Get the dictionary values as a list
print('values as a list : ', list(student.values()))

# 9. Change the dictionary to a list of tuples using items()
print('as a list of tuples : ', list(student.items()))

# 10. Delete one of the items in the dictionary
student.pop('age')  # or del student['age']
print('student without age : ', student)

# 11. Delete one of the dictionaries
del dog
try:
    print(dog)
except NameError:
    print('dog has been deleted')