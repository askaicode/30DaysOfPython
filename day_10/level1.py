# level1 : Loops : while and for loops
# 1. iterate 0 to 10 with for loop and while
# for loop 0 -> 10
print('For Loop : ')
for i in range(11):
    print(i)
# while loop 0 -> 10
print('While Loop :')
i = 0
while i < 11:
    print(i)
    i += 1
# 2. 10 -> 0
print('10 to 0')
for i in range(10, -1, -1):
    print(i)
print('while : 10 -> 0')
i = 10
while i > -1:
    print(i)
    i -= 1
# 3. getting on the ouput the following triangle
print('-----------------------------------')
char = '#'
for i in range(1, 8):
    print(char * i)
# 4. using nested loops
print('-----------------------------')

for r in range(8):
    for c in range(8):
        print('#', end=' ')
    print()

# 5. print the following pattern
print('----------------------------------')
for i in range(11):
    print(f'{i} x {i} = {i * i}')

# 6. Iterating through the list
print('----------------------------')
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in lst:
    print(item)

# 7. For loop from 0->100 only the even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

# 8. For loop from 0->100 only odd numbers
for i in range(101):
    if i % 2 == 1:
        print(i)

# or

'''for i in range(0, 101, 2):   # even numbers
    print(i)

for i in range(1, 101, 2):   # odd numbers
    print(i)    
'''
