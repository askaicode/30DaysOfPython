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
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# new_countries = []
# print('first : ', countries)
# for item in countries:
#     row = []
#     for k in item:
#         for v in k:
#             row.append(v.upper())
#     row.insert(1, row[0][:3])
#     new_countries.append(row)
# print(new_countries)

# numbers = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = [
#     number * 2
#     for row in numbers
#     for number in row
#     if number > 4
# ]


# # '''
# - row contains: [1, 2, 3]
# - number:
# 1st iteration: 1 then before adding number to result is the current iteration value greaten than 4?
# if True : add the current number to result
# then pass to the next number whihc is 2... and so on
# if the first row is done
# pass to the next row
# and so on....

# so the result will be : [10, 12, 14, 16, 18]

# '''


# level 3
# students = [
#     [('John', 15), ('Mary', 18)],
#     [('David', 12), ('Sarah', 20)],
#     [('Peter', 16), ('Alice', 14)]
# ]

'''

first inner loop iteration:
    [('John', 15), ('Marry', 18)]
        first iteration in inner loop:
            name: John score: 15
        we use for name, score in group because we need key(name) and value(score)
        if score greater or equal 16 add the name upper version to the new list
        second iteration in inner loop:
            name: Marry score: 18
final output:
    ['MARRY', 'SARAH', 'PETER']
'''

# products = [
#     [('Laptop', 1200), ('Mouse', 25)],
#     [('Keyboard', 80), ('Monitor', 300)],
#     [('Phone', 900), ('USB', 10)]
# ]

# new_product = [
#     [name.upper(), price] 
#     for product in products for name, price in product
#     if price >= 80
# ] 
# print(new_product)

# employees = [
#     [
#         ('John', 25, 2500),
#         ('Mary', 30, 3500)
#     ],
#     [
#         ('David', 22, 1800),
#         ('Sarah', 28, 4000)
#     ],
#     [
#         ('Peter', 35, 4500),
#         ('Alice', 24, 2200)
#     ]
# ]

# new_employee = [
#     [name.upper(), salary]
#     for employee in employees
#     for name, age, salary in employee
#     if age >= 25 and salary > 3000
# ]

# print(new_employee)

# students = [
#     ('John', 80),
#     ('Mary', 95),
#     ('David', 65),
#     ('Sarah', 90)
# ]

# new_students = {
#     name: score
#     for name, score in students
#     if score >= 80
# }

# print(new_students)

# products = [
#     ('Laptop', 1200),
#     ('Mouse', 25),
#     ('Keyboard', 80),
#     ('Monitor', 300)
# ]

# new_products = {
#     name.upper(): price
#     for name, price in products
# }

# print(new_products)

# departments = [
#     [('John', 2500), ('Mary', 3500)],
#     [('David', 1800), ('Sarah', 4000)]
# ]

# new_products = {
#     name.upper(): salary
#     for department in departments
#     for name, salary in department
#     if salary > 2000
# }

# print(new_products)

def get_bonus(salary):
    return salary * 0.1

print(get_bonus(2500))

employees = [
    ('John', 2500),
    ('Mary', 3500),
    ('David', 1800),
    ('Sarah', 4000)
]

new_employees = {
    name: get_bonus(salary)
    for name, salary in employees
    if salary > 2000
}

print(new_employees)

def calculate_salary(items):
    return {
        name: salary + get_bonus(salary)
        for name, salary in items
        if salary >= 2500
    }

print(calculate_salary(employees))