# Level 1
import math
# 1 add_two_numbers()
def add_two_numbers(n1, n2):
    return n1 + n2
print(add_two_numbers(2, 5))

# 2 area of a circle area = PI * r * r
def area_of_circle(r):
    return math.pi * r * r
print(area_of_circle(10))

# 3 add_all_nums
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
        else:
            return f'{num} is not a number'
    return total
print(add_all_nums(1, 2.5, 4))
print(add_all_nums(1, 'dd', 4))

# 4 °F = (°C x 9/5) + 32
def convert_celsius_to_fahrenheit(c):
   return (c * 9 / 5) + 32
print(convert_celsius_to_fahrenheit(20))
print(convert_celsius_to_fahrenheit(37))

# 5 check_season(month)
'''
• Spring: March, April, May
• Summer: June, July, August
• Autumn (also called Fall): September, October, November
• Winter : December, January, February
'''

def check_season(month):
    month = str(month).capitalize()
    if month in ('March', 'April', 'May'):
        return 'Spring'
    elif month in ('June', 'July', 'August'):
        return 'Summer'
    elif month in ('September', 'October', 'November'):
        return 'Autumn'
    elif month in ('December', 'January', 'February'):
        return 'Winter'
    return 'Unknown'
print(check_season('june'))

# 6 slope between two points: (y2 - y1) / (x2 - x1)
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return 'The slope is undefined (vertical line)'
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1, 2, 3, 6))   # 2.0
# 7 solve_quadratic_eqn
# 7 ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return 'Not a quadratic equation (a cannot be 0)'
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'No real solutions'
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return (x1, x2)
print(solve_quadratic_eqn(1, -3, 2))   # (2.0, 1.0)

# 8 print_list
def print_list(items):
    for item in items:
        print(item)
print_list(['abala', 'balace', 'calace'])

# 9 reverse_list
def reverse_list(items):
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(['A', 'B', 'C']))

# 10 capilaze_list_items
def capitalize_list_items(items):
    result = []
    for item in items:
        result.append(item.capitalize())
    return result
print(capitalize_list_items(['allo', 'oka', 'mala']))

# 11 add_item
def add_item(items, item):
    new_list = items.copy()
    new_list.append(item)
    return new_list
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12 remove_item
def remove_item(items, item):
    new_list = items.copy()
    if item in new_list:
        new_list.remove(item)
    return new_list
print(remove_item(food_stuff, 'Mango'))
print(remove_item(numbers, 3))

# 13 sum_of_numbers
def sum_of_numbers(number):
    total = 0
    for i in range(number + 1):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

# 14 sum_of_odds
def sum_of_odds(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 1:
            total += i
    return total
print(sum_of_odds(5))

# 15 sum_of_even
def sum_of_even(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(5))