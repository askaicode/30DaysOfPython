# ---------------------------------------------------------------
# YOUR TURN (write these below)
# ---------------------------------------------------------------
# 1. Use int(input('Enter a number: ')) inside try/except ValueError.
import os

while True:
   try:
       n = int(input('Enter a number: '))
   except ValueError:
       print('Not a number. Try again !')
   else:
       print('Number is : ', n)
       break

#    Print 'Not a number' if the user types text.
# 2. Make a dictionary {'a': 1} and read key 'b' inside try/except KeyError.
my_dict = {'a': 1}
try:
    print(my_dict['b'])
except KeyError:
    print('Key "b" does not exist')

# 3. Make a list [1, 2, 3] and read index 10 inside try/except IndexError.
numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:
    print('Index 10 is out of range')
# 4. Write a function safe_open(path) that returns the file's text,
def safe_open(path):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f'File not found : {path}'
print(safe_open('./data/michelle_obama_speech.txt'))
#    or the string 'file not found' if the file does not e
print('still running...')