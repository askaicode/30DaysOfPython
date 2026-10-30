# Level 2
# 1. Give grade to students according to their scores
score = int(input('Enter your score: '))
if score < 0 or score > 100:
    print('Invalid score')
elif score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Grade: F')

# 2. Get the month from user input and find the season
month = input('Enter the month: ').strip().capitalize()
if month in ('September', 'October', 'November'):
    print('Season: Autumn')
elif month in ('December', 'January', 'February'):
    print('Season: Winter')
elif month in ('March', 'April', 'May'):
    print('Season: Spring')
elif month in ('June', 'July', 'August'):
    print('Season: Summer')
else:
    print('Invalid month')

# 3. Add a fruit to the list if it doesn't exist
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Enter a fruit: ').strip().lower()
if fruit not in fruits:
    fruits.append(fruit)
    print('Modified list:', fruits)
else:
    print('That fruit already exist in the list')