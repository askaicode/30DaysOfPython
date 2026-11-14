# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [ i for i in numbers if i <= 0 ]
print(neg_and_zero)

# 2
lists_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_in_one = [ i for row in lists_of_lists for i in row ]
print(all_in_one)

# 3
my_list = [ (i, i ** 0, i**1, i**2, i**3, i**4, i**5) for i in range(11) ]
print(my_list)

# 4
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]
]

new_countries = [
    [country.upper(), country.upper()[:3], city.upper()]
    for group in countries
    for country, city in group
]

print(new_countries)

# 5
countries_dict = [
    {'country': country.upper(), 'city': city.upper()}
    for group in countries
    for country, city in group
]

print(countries_dict)

# 6
names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]

new_names = [
    f'{firstname} {lastname}'
    for name in names
    for firstname, lastname in name
]

print(new_names)

# 7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1