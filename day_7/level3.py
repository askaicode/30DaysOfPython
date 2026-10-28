# Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Convert the ages to a set and compare the length of the list and the set
age_set = set(age)
print(type(age_set))
print(len(age), len(age_set))  # 8 5
print(age_set)
# a set removes duplicates, so its length is smaller

print('Are list length and set length the same : ', len(age) == len(age_set))  # False
print('Which one is bigger : the list')

# 2. Explain the difference between the following data types

# string: ordered sequence of characters, immutable, indexed
name = 'askaicode'
print(name[0])
# name[0] = 'A'  # TypeError: strings do not support item assignment
name = 'taletsy'  # this only re-assigns the variable to a new string

# list: ordered, mutable, indexed, allows duplicates
fruits = ['apple', 'banana', 'cherry']
fruits[-1] = 'durian'
print('fruits : ', fruits)

# tuple: ordered, immutable, indexed, allows duplicates
person = ('john', 'jim', 'joe', 'john')
print(person[0])
# person[0] = 'keve'  # TypeError: tuples do not support item assignment
print('tuple : ', person)

# set: unordered, mutable (add/remove), no indexes, unique items only
users = {'hello', 'allo', 'ellas', 'allo', 'allo'}
users.add('new')
print('users : ', users)
# print(users[0])  # TypeError: sets are not indexed

# 3. I am a teacher and I love to inspire and teach people.
sentence = 'I am a teacher and I love to inspire and teach people'
sentence_list = sentence.split()
print('list : ', sentence_list)
sentence_set = set(sentence_list)
print('set : ', sentence_set)
print('Original words count : ', len(sentence_list))  # 12
print('Unique words count : ', len(sentence_set))      # 10
print('Are the original length and the unique the same : ',
      len(sentence_set) == len(sentence_list))          # False