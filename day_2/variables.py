#Day 2 : 30 Days of python programming

first_name =  'Askaicode'
last_name = 'Taletsy'
full_name = 'Askaicode Taletsy'
country = 'Madagascar'
city = 'Antananarivo'
age = 24
year = 2026
is_married = False
is_true = True
is_light = True
x, y, z = 1, 2, 3

#exercises : Level2

#1 data type checking

print(type(first_name), type(last_name), type(full_name), type(country), type(city), type(age), type(year),type(is_married))
print(type(is_true), type(is_light), type(x), type(y), type(z))
#2 using len

print('first name lenght :', len(first_name))
#3 comparing first_name vs last_name lenght

first_name_len = len(first_name)
last_name_len = len(last_name)
print('comparing firstname vs lastname lenght')
print('first name : ', first_name_len)
print('last name : ', last_name_len)

#4
num_one, num_two = 5, 10
#5
total = num_one + num_two
#6
diff = num_two - num_one
#7
product = num_two * num_one
#8
division = num_one / num_two
#9
remainder = num_two % num_one
#10
exp = num_one ** num_two
#11
floor_division = num_one // num_two
#12 Circle
### are of circle : radius r = 30meters
"""area = r * r * PI
    circumference = 2 * PI * r
"""
_radius = 30
_PI = 3.14
area_of_circle = (_radius ** 2) * _PI
print('area of circle : ', area_of_circle)
circum_of_circle = 2 * _PI * _radius
print('circumference : ', circum_of_circle)

#take radius from user
user_radius = int(input('Enter radius of circle : '))
user_area_of_circle = (user_radius ** 2) * _PI
user_circum_of_circle = 2 * _PI * user_radius
print('area of circle : ', user_area_of_circle)
print('circumference : ', user_circum_of_circle)

#13 get user info using input function
first_name = input('What is you first name : ')
last_name = input('Enter your last name : ')
country = input('Enter your country name : ')
age = input('Enter your age : ')

