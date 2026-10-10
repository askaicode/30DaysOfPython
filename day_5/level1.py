# 1 empty list 
empty_list = []
# 2 a list with more than 5 items
customers = ['Heram', 'jamal', 'rocks', 'jenny', 'kiffr', 'hello']
# 3 find the length of a list
len_customer = len(customers)
print('customer\'s length : ', len_customer)
# 4 Get
first_customer = customers[0]
middle_customer = customers[(len_customer // 2)]
last_customer = customers[-1]
print('first item : ', first_customer)
print('middle item : ', middle_customer)
print('last item : ', last_customer)
# 5
mixed_data_types = ['askaicode', 24, 178, 'single', 'Antananarivo Madagascar']
# 6 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7
first_comp = it_companies[0]
middle_comp = it_companies[(len(it_companies) // 2)]
last_comp = it_companies[-1]
# 8
number_of_companies = len(it_companies)
print('number of companies : ', number_of_companies)
# 9
print('first company : ', first_comp)
print('middle company : ', middle_comp)
print('last company : ', last_comp)
# 10
it_companies[0] = 'Askaicode'
print(it_companies)
# 11
it_companies.append('HelloCode')
# 12
middle_index = (len(it_companies) // 2)
print('middle index : ', middle_index)
it_companies.insert(middle_index, 'middle_companies')
print(it_companies)
# 13
idx = it_companies.index('Amazon')
it_companies[idx] = it_companies[idx].upper()
print('upper one item : ', it_companies)
# 14    
joined_it_list = '#;  '.join(it_companies)
print('joined IT list : ', joined_it_list)
# 15
does_exist = 'Tesla' in it_companies
print(f'Does tesla exist in IT companies : {does_exist}')
# 16
it_companies.sort()
print('Ascending IT list : ', it_companies)
# 17
it_companies.reverse()
print('Reversed IT list : ', it_companies)
# 18
first_3_companies = it_companies[ : 3]
print('First three companies : ', first_3_companies)
# 19
last_3_companies = it_companies[-3 : ]
print('Last three companies : ', last_3_companies)