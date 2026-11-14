# Day 14: level1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
# map: applies a function to every item, returns an iterable of the same length
# filter: keeps only the items for which the function returns True (can be shorter)
# reduce: combines all items into a single value, using a function with two parameters
#         (result so far, next item). Needs: from functools import reduce

# 2
# higher order function: takes a function as a parameter and/or returns a function
# closure: an inner function that remembers variables of its outer function
# decorator: a function that wraps another function to add behavior without changing it
# 3 - Define a call function before map, filter or reduce, see examples
from functools import reduce

# 3 - Define a function before map, filter, reduce
def change_to_upper(name):
    return name.upper()

def is_name_long(name):
    return len(name) > 7

def add_two_nums(x, y):
    return x + y

print(list(map(change_to_upper, names)))   # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
print(list(filter(is_name_long, names)))   # ['Asabeneh']
print(reduce(add_two_nums, numbers))       # 55

# 4 - Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5 - Use for to print each name in the names list.
for name in names:
    print(name)

# 6 - Use for to print each number in the numbers list.
for number in numbers:
    print(number)
    