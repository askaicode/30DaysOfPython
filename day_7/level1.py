# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. the length of the set it_companies
len_it_companies = len(it_companies)
print('the length of the set it companies is : ', len_it_companies)

# 2. Adding 'Twitter to it_companies
it_companies.add('Twitter')

# 3. Inserting multiple IT companies at once to the set it_companies
it_companies.update({'Askaicode', 'Meta', 'Alibaba'})
print(it_companies)

# 4. Removing one of the companies from the set it_companies
it_companies.remove('Meta') # the element must be a member (raise an exception)
print(it_companies)

# 5. difference between remove and discard
it_companies.discard('Alibaba') # no exception even the element is missing from the set.
print(it_companies)


# Answer to question 5
# remove(x) raises a KeyError if x is not in the set.
# discard(x) does nothing if x is not in the set.

# Use discard when you don’t care whether the item exists, and remove when a missing item should be treated as an error.

