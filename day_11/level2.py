# # Level 2 
# # 1 
# from math import sqrt
# def evens_and_odds(number):
#     even = 0
#     odd = 0
#     for i in range(number + 1):
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return f'The number of odds are {odd} \nThe number of evens are {even}'
# print(evens_and_odds(100))

# def factorial(number):
#     result = 1
#     for i in range(number, 1, -1):
#         result *= i
#     return result
# print(factorial(4))
# print(factorial(0))

# # 2
# def is_empty(value):
#     if value is None:
#         return True
#     if isinstance(value, (str, list, tuple, dict, set)):
#         return len(value) == 0
#     return False
# print(is_empty(''))

# # 3 
# def calculate_mean(items):
#     total = 0
#     for item in items:
#         total += item
#     count = len(items)
#     return total / count
# print('The mean of  2, 4, 6, 8, 10, 12, 14, 16 is ', calculate_mean([2, 4, 6, 8, 10, 12, 14, 16]))

# # def calculate_mean(items):
# #     return sum(items) / len(items)

# def calculate_median(items):
#     sorted_items = sorted(items)
#     n = len(sorted_items)
#     mid = n // 2
#     if n % 2 == 0:
#         return (sorted_items[mid - 1] + sorted_items[mid]) / 2
#     return sorted_items[mid]

# print('Median:', calculate_median([3, 1, 7, 4, 2]))   # 3
# print('Median:', calculate_median([3, 5, 7, 19]))     # 6.0

# def calculate_mode(items):
#     count = {}
#     # {count: item}
#     for item in items:
#         count[item] = count.get(item, 0) + 1
#     pairs = []
#     for name in count:
#         pairs.append((count[name], name))
#     _max = max(pairs)[0]
#     max_items = []
#     for item in pairs:
#         if item[0] == _max:
#             max_items.append(item)
#     return max_items
# print(calculate_mode([5, 5, 4, 2]))


# # def calculate_mode(items):
# #     counts = {}
# #     for item in items:
# #         counts[item] = counts.get(item, 0) + 1
# #     highest = max(counts.values())
# #     return [item for item, c in counts.items() if c == highest]


# def calculate_range(items):
#     return max(items) - min(items)
# print(calculate_range([5, 12, 8, 24, 15]))

# def calculate_variance(items):
#     ln = len(items)
#     total = 0
#     for item in items:
#         total += item
#     average = total / ln
#     subtracted_items = []
#     for item in items:
#         subtracted_items.append(item - average)
#     squared_items = []
#     for item in subtracted_items:
#         squared_items.append(item ** 2)
#     total_sq = 0
#     for item in squared_items:
#         total_sq += item
#     return round(total_sq / (ln - 1), 2)
# print(calculate_variance([2, 4, 4, 4, 5, 5, 7, 9]))

# def calculate_std_dev(items):
#     return round(sqrt(calculate_variance(items)), 2)
# print(calculate_std_dev([2, 4, 4, 4, 5, 5, 7, 9]))

# # 4
# def greet(name = 'Guest'):
#     return f'Hello, {name}!'
# print(greet())

# # 5
# def show_args(**keywd):
#     for key, value in keywd.items():
#         print(f'Received: {key}: {value}', end=' ')
#     print()
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny

# Level 2
from math import sqrt

# 1
def evens_and_odds(number):
    even = 0
    odd = 0
    for i in range(number + 1):   # 0 counts as even
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f'The number of odds are {odd}.\nThe number of evens are {even}.'

print(evens_and_odds(100))


def factorial(number):
    result = 1
    for i in range(number, 1, -1):
        result *= i
    return result

print(factorial(4))   # 24
print(factorial(0))   # 1


# 2
def is_empty(value):
    if value is None:
        return True
    if isinstance(value, (str, list, tuple, dict, set)):
        return len(value) == 0
    return False

print(is_empty(''))      # True
print(is_empty([1, 2]))  # False


# 3
def calculate_mean(items):
    return sum(items) / len(items)

print('Mean:', calculate_mean([2, 4, 6, 8, 10, 12, 14, 16]))   # 9.0


def calculate_median(items):
    sorted_items = sorted(items)
    n = len(sorted_items)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_items[mid - 1] + sorted_items[mid]) / 2
    return sorted_items[mid]

print('Median:', calculate_median([3, 1, 7, 4, 2]))   # 3
print('Median:', calculate_median([3, 5, 7, 19]))     # 6.0


def calculate_mode(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    highest = max(counts.values())
    return [item for item, c in counts.items() if c == highest]

print('Mode:', calculate_mode([5, 5, 4, 2]))   # [5]
print('Mode:', calculate_mode([1, 1, 2, 2]))   # [1, 2]


def calculate_range(items):
    return max(items) - min(items)

print('Range:', calculate_range([5, 12, 8, 24, 15]))   # 19


def calculate_variance(items):
    mean = calculate_mean(items)
    squared_diffs = [(x - mean) ** 2 for x in items]
    return sum(squared_diffs) / len(items)   # population variance
    # for sample variance use: / (len(items) - 1)

print('Variance:', calculate_variance([2, 4, 4, 4, 5, 5, 7, 9]))   # 4.0


def calculate_std(items):
    return sqrt(calculate_variance(items))

print('Std:', calculate_std([2, 4, 4, 4, 5, 5, 7, 9]))   # 2.0


# 4
def greet(name='Guest'):
    print(f'Hello, {name}!')

greet()          # Hello, Guest!
greet('Alice')   # Hello, Alice!


# 5
def show_args(**kwargs):
    print(kwargs.items())
    pairs = [f'{key}: {value}' for key, value in kwargs.items()]
    print('Received: ' + ', '.join(pairs))
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny