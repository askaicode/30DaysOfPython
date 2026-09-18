# print('Days\tTopics\tExercises')
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('This is a backslash symbol (\\\\)')
# print('In every programming language it starts with \"Hello, World!\"')
# print('I hope every one is enjoying the Python Challenge.\nAre?')
# # String only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # String and numbers
# radius  = 10
# pi = 10
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.3f.' %(radius, area)

# print(formated_string)
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']

# formated_string = 'The following are python libraries: %s' %(python_libraries)
# print(formated_string)

# formated_string = 'I am {} {}, I teach {}'.format(first_name, last_name, language)
# print(formated_string)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b))
# print('{} % {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# # Strings and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of a circle with a radius {} is {:.2f}'.format(radius, area)
# print(formated_string)

# a = 4
# b = 3
# print('String interpolation')
# print(f'{a} + {b} = {a + b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')

# print('Unpacking Characters')
# language = 'Python'
# a, b, c, d, e, f = language
# print(a, b, c, d, e, f)
# first_letter = language[0]
# last_index = len(language) - 1
# last_letter = language[last_index]
# print('Last letter is : ', last_letter)

# # Slicing Python String

# first_tree = language[0:3]
# print(first_tree)
# last_three = language[3:6]
# print(last_three)
# # Another way
# last_three = language[-3:]
# print(last_three)
# last_tree = language[3:]
# greeting = 'Hello, World!'
# reversed_greeting = greeting[::-1]
# print(reversed_greeting)

# skiped_word = language[0:6:2]
# print('Skipped word : ', skiped_word)
# challenge = 'thirty days of Python.'
# print(challenge.capitalize())
# print(challenge.count('f'))
# print(challenge.count('y', 7, 14))
# print(challenge.endswith('on.'))
challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs(4))
print(challenge.rfind('y'))
sub_string = 'da'
sub_string_2 = 'py'
print(challenge.index(sub_string))
print(challenge.index(sub_string_2, 9))
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '-'.join(web_tech)
print(result)

challenge = 'thirty days of python'
print(challenge.strip('thnni')) #irty days of pythoo
print(challenge.replace('python', 'coding'))
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))
print(challenge.title())
print(challenge.swapcase())
print(challenge.startswith('th'))
print(challenge.endswith('on'))