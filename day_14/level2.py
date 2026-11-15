# Level 2
from functools import reduce
from countries import countries_data
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1 
def change_to_upper(country_name):
    return country_name.upper()

print(list(map(change_to_upper, countries)))

# 2
def square(number):
    return number ** 2

print(list(map(square, numbers)))

# 3
def change_name_to_upper(name):
    return name.upper()

print(list(map(change_name_to_upper, names)))

# 4
def does_contain_land(country_name):
    if 'land' in country_name.lower():
        return True
    return False

print(list(filter(does_contain_land, countries)))

# 5
def does_have_six_chars(country_name):
    return len(country_name) == 6  

print(list(filter(does_have_six_chars, countries)))

# 6
def does_have_at_least_six(country_name):
    if len(country_name) >= 6:
        return True
    return False

print(list(filter(does_have_at_least_six, countries)))

# 7
def start_with_e(country_name):
    if country_name[0].lower() == 'e':
        return True
    return False

print(list(filter(start_with_e, countries)))

# 8
print(reduce(lambda a, b: a + b, list(filter(lambda n: n > 50, list(map(square, numbers))))))

# 9
mix_list = numbers + countries
def is_string(item):
    if type(item) == str:
        return True
    return False

def get_string_lists(items):
    return list(filter(is_string, items))

print(get_string_lists(mix_list))

# 10
total = reduce(lambda a, b: a + b, numbers)
print(total)

# 11
# res = reduce(lambda a, b: f'{a} , {b} are north European countries', countries)
# print(res)
def join_countries(a, b):
    return f'{a}, {b}'

first_part = reduce(join_countries, countries[:-1])
sentence = f'{first_part}, and {countries[-1]} are north European countries'
print(sentence)

# 12 Declare a function called categorize_countries
# that returns a list of countries with some common pattern
def categorize_countries(data, pattern):
    res = list(filter(lambda country: pattern in country.lower(), data))
    return res

print(categorize_countries(countries_data, 'stan'))

# 13 Create a function returning a dictionary, 
# where keys stand for starting letters of countries 
# and values are the number of country names starting with that letter.

def create_dict_from_list(items):
    res = {}
    for item in items:
        key = item[0].upper()
        res[key] = res.get(key, 0) + 1
    return res

print(create_dict_from_list(countries_data))

# 14 Declare a get_first_ten_countries function -
# it returns a list of first ten countries from the countries.js list
# in the data folder.

def get_first_ten_countries(items):
    return items[:10]

print(get_first_ten_countries(countries_data))

# 15 Declare a get_last_ten_countries function
# that returns the last ten countries in the countries list.
def get_last_ten_countries(items):
    return items[-10:]

print(get_last_ten_countries(countries_data))