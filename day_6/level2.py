from level1 import family_members

# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print(father, mother)

# 2. Create fruits, vegetables and animal products tuples, then join them
fruits = ('apple', 'banana', 'orange', 'mango')
vegetables = ('carrot', 'potato', 'cabbage', 'broccoli')
animal_products = ('milk', 'eggs', 'honey')
food_stuff_tp = fruits + vegetables + animal_products

# 3. Convert the tuple to a list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item(s)
n = len(food_stuff_lt)
mid = n // 2
if n % 2 == 1:                              # odd length -> one middle item
    middle_items = food_stuff_lt[mid]
else:                                       # even length -> two middle items
    middle_items = food_stuff_lt[mid - 1:mid + 1]
print('Middle item(s):', middle_items)

# 5. Slice out the first three and the last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three, last_three)

# 6. Delete the food_stuff_tp tuple
del food_stuff_tp

# 7. Check if an item exists in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Is Estonia a Nordic country?', 'Estonia' in nordic_countries)   # False
print('Is Iceland a Nordic country?', 'Iceland' in nordic_countries)   # True