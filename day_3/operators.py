import math

# 1 to 4
'''age = 24
height = 177.50
complex_number = 4 + 4j
base = int(input('Enter the base of the triangle : '))
height = int(input('Enter the height of the triangle : '))
area_of_triangle = int(0.5 * base * height)
print('The area of the triangle is ', area_of_triangle)
# Triangle perimeter
a = int(input('Enter side a : '))
b = int(input('Enter side b : '))
c = int(input('Enter side c : '))
perimeter_of_triangle = a + b + c
print('The perimeter of the triangle is ', perimeter_of_triangle)
'''
# 6 Calculate rectangle area = length * width
# perimeter = 2 * (length + width)
'''width = int(input('Enter the width : '))
length = int(input('Enter the length : '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)
print('The area of rectangle is : ', area_of_rectangle)
print('The perimeter of rectangle is : ', perimeter_of_rectangle)

# 7 Circle : area = pi * r * r, circumference = 2 * pi * r where pi + 3.14
PI = 3.14
radius = float(input('Enter the radius of circle : '))
area_of_circle = PI * radius * radius
print('The area of circle is : ', area_of_circle)
circumference = 2 * PI * radius
print('The circumference of circle is : ', circumference)
'''

# 8 Calculating slope, x-intercept and y-intercept of y = 2x - 2
# y = mx + b
m_8 = 2
b = -2
x_intercept = -(b) // m_8
y_intercept = b

print('Slope(m) : ', m_8) # m = 2
print('x-intercept : ', x_intercept) #(1, 0)
print('y-intercept : ', y_intercept) #(0, -2)

# 9 - Slope is (m = y2-y1/x2-x1)
# # Find the slope
y1 = 2
y2= 10
x2 = 6
x1 = 2
m_9 = (y2 - y1) // (x2 - x1)
print('Slope if task9 is : ', m_9)
# Euclidean distance between point (2, 2) and point (6,10)
# The formula: distance = square root of ((x2 - x1)² + (y2 - y1)²)
distance_euclidean = round(math.sqrt((y2 - y1)**2 + (x2 - x1)**2), 2)
print('The distance euclidean is : ', distance_euclidean)

# 10 - comparing m_8 and m_9
print('Comparing m_8 and m_9 (==)', m_8 == m_9)
print('Comparing m_8 and m_9 (>)', m_8 > m_9)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# 11 - y = x**2 + 6x + 9
# for y = 0, x should be -3
x = -3
y = (x**2) + 6 * x + 9
print('x : ', x)
print('y : ', y)

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_len = len('python')
dragon_len = len('dragon')
print('Fasly comparaison of python and dragon with !=', python_len != dragon_len)
print('Fasly comparaison of python and dragon with >', python_len > dragon_len)

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'
word1  = 'python'
word2 = 'dragon'
print('on' in word1 and 'on' in word2)

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon.'
target_word = 'jargon'
print(target_word in sentence)

# 15 There is no 'on' in both dragon and python
print('There no "on" in both dragon and python : ')
found_on = 'on' in word1 and 'on' in word2
print(not found_on)

# 16 Find the length of the text python and convert the value to float and convert it to string
python_len_float = float(python_len)
python_len_string = str(python_len)
print(python_len_float, python_len_string)

# 17 - Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
test_number = 18
remainder = test_number % 2
print(remainder == 0)

# 18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_converted = int(2.7)
is_the_same = floor_division == int_converted
print(is_the_same)

#19 - Check if type of '10' is equal to type of 10
type1 = type('10')
type2 = type(10)
print('is the same type : ', type1 == type2)

# 20 - Check if int('9.8') is equal to 10
int_9dot8 = int(float('9.8'))
print('is the same : ', int_9dot8 == 10)

# 21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
worked_hours = float(input('Enter worked hours : '))
rate_per_hour = float(input('Enter rate per hour : '))
weekly_salary = round(worked_hours * rate_per_hour, 2)
print('Your weekly earning is : ', weekly_salary)

# 22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# Seconds = Years x 31,536,000
sec_per_year = 31536000
years_lived = int(input('Enter number of years you have lived : '))
years_in_sec = years_lived * sec_per_year
print('You have lived for ', years_in_sec, 'seconds.')