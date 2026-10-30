# 1. Get user input using input
age_qualified = 18
age = int(input('Enter your age: '))
missing_year = age_qualified - age
if age >= age_qualified:
    print('You are old enough to learn to drive.')
else:
    print(f"You need {missing_year} more year{'s' if missing_year > 1 else ''} to learn to drive.")

# 2. Compare my_age and your_age
my_age = 25
your_age = int(input('Enter your age: '))
diff = abs(my_age - your_age)
if my_age == your_age:
    print('We are the same age.')
elif your_age > my_age:
    if diff == 1:
        print(f'You are {diff} year older than me.')
    else:
        print(f'You are {diff} years older than me.')
else:
    if diff == 1:
        print(f'You are {diff} year younger than me.')
    else:
        print(f'You are {diff} years younger than me.')

# 3. Get two numbers from the user using input prompt
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')