# # Level 3
# from countries_data import countries_data
# '''
# greater than 1 and 
# divisible only by 1 and itself.
# '''
# # 1

# def is_prime(number):
#     divisors = []
#     if number > 1:
#         for n in range(1, number + 1):
#             if number % n == 0:
#                 divisors.append(n)
#         return len(divisors) == 2
#     else:
#         return False

# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(5))
# print(is_prime(7))
# print(is_prime(9))
# print(is_prime(1))

# # 2
# def with_unique_items(items):
#     count = {}
#     for n in items:
#         count[n] = count.get(n, 0) + 1
#     duplicated = 0
#     for n in count:
#         if count[n] > 1:
#             duplicated += 1
#     return duplicated == 0
# print('with unique items : ')
# print(with_unique_items([1, 1, 2, 4, 3]))
# print(with_unique_items([1, 2, 4, 3, 3]))
# print(with_unique_items([1, 2, 4, 3]))

# # 3
# def same_data_type(items):
#     prev = type
#     for i in range(len(items)):
#         if i == 0:
#             prev = type(items[i])
#         if i >= 1:
#             if prev == type(items[i]):
#                 prev = type(items[i])
#             else:
#                 print('stop at index : ', i, items[i])
#                 return False
#     return True
# print('same data type')
# print(same_data_type([1, 'a', 'b']))

# # 4
# def is_valid_variable_name(variable):
#     return variable.isidentifier()
# var = '123'
# print('is valid variable name : ', is_valid_variable_name(var))

# # 5
# def most_spoken_languages(items, limit):
#     languages = [item['languages'] for item in items]
#     result = [item for language in languages for item in language]
#     # for language in languages:
#     #     for item in language:
#     #         result.append(item)
#     count = {}
#     for name in result:
#         count[name] = count.get(name, 0) + 1
#     pairs = [(count[item], item) for item in count]
#     pairs.sort(reverse=True)
#     char = ''
#     for count, name in pairs[:limit]:
#         char += f'{name} : {count} \n'
#     return char

# print(most_spoken_languages(countries_data, 10))
# print(most_spoken_languages(countries_data, 20))

# #
# def most_populated_countries(items, limit):
#     populations = [(item['population'], item['name']) for item in items]
#     populations.sort(reverse=True)
#     char = ''
#     for population, countrie in populations[:limit]:
#         char += f'{countrie}: {population} \n'
#     return char
# print(most_populated_countries(countries_data, 10))

# Level 3
import keyword
from countries_data import countries_data   # file must be named countries_data.py


# 1
def is_prime(number):
    if number < 2:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False   # found a divisor, so not prime
    return True

for n in [1, 2, 3, 5, 7, 9, 97]:
    print(n, is_prime(n))   # False, True, True, True, True, False, True


# 2
def has_unique_items(items):
    return len(items) == len(set(items))

print(has_unique_items([1, 1, 2, 4, 3]))   # False
print(has_unique_items([1, 2, 4, 3]))      # True


# 3
def same_data_type(items):
    if len(items) == 0:
        return True
    first_type = type(items[0])
    for item in items:
        if type(item) != first_type:
            return False
    return True

print(same_data_type([1, 2, 3]))        # True
print(same_data_type([1, 'a', 'b']))    # False


# 4
def is_valid_variable_name(name):
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_variable_name('first_name'))   # True
print(is_valid_variable_name('123'))          # False
print(is_valid_variable_name('first-name'))   # False
print(is_valid_variable_name('for'))          # False (keyword)


# 5
def most_spoken_languages(items, limit):
    counts = {}
    for country in items:
        for language in country['languages']:
            counts[language] = counts.get(language, 0) + 1

    pairs = [(count, language) for language, count in counts.items()]
    pairs.sort(reverse=True)   # highest count first
    return [(language, count) for count, language in pairs[:limit]]

for language, count in most_spoken_languages(countries_data, 10):
    print(f'{language}: {count}')


def most_populated_countries(items, limit):
    pairs = [(country['population'], country['name']) for country in items]
    pairs.sort(reverse=True)
    return [(name, population) for population, name in pairs[:limit]]

for name, population in most_populated_countries(countries_data, 10):
    print(f'{name}: {population}')