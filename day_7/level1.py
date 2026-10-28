# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print('Length of it_companies:', len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# 3. Insert multiple IT companies at once
it_companies.update(['Askaicode', 'Meta', 'Alibaba'])
print(it_companies)

# 4. Remove one of the companies
it_companies.remove('Meta')
print(it_companies)

# 5. Difference between remove and discard
# Both delete an item from the set. The difference shows when the item is missing:
it_companies.discard('Netflix')       # no error, the set is unchanged
print('discard on a missing item: no error')

try:
    it_companies.remove('Netflix')    # raises KeyError
except KeyError:
    print("remove on a missing item: KeyError")

'''
Answer to question 5
remove(x) raises a KeyError if x is not in the set.
discard(x) does nothing if x is not in the set.

Use discard when you don’t care whether the item exists, and remove when a missing item should be treated as an error.
'''