# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'
# 4 print var using print()
print(company)
# 5 Print the length of the company string using len() method and print().
company_len = len(company)
print('Company length is : ', company_len)
# 6 Change all the characters to uppercase letters using upper() method.
company_uppercased = company.upper()
print('result : ', company_uppercased)
# 7 Change all the characters to lowercase letters using lower() method.
company_lowercased = company.lower()
print('result : ', company_lowercased)
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalzed_str = company.capitalize()
titled_str = company.title()
swapcased_str = company.swapcase()
print(capitalzed_str, titled_str, swapcased_str)
# 9 Cut(slice) out the first word of Coding For All string.
first_word = company.split(' ')[0]
print('The first world : ', first_word)
# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
position_coding = company.index('Coding')
found_word = company.find('Coding')
print(position_coding)
print(found_word)
# 11 Replace the word coding in the string 'Coding For All' to Python.
new_sentence = company.replace('Coding', 'Python')
print(new_sentence)
# 12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
old_phrase = 'Python for Everyone'
new_phrase = old_phrase.replace('Everyone', 'All')
print(new_phrase)
# 13 Split the string 'Coding For All' using space as the separator (split()) .
new_list = company.split(' ')
print(new_list)
# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
str1 = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(str1.split(', '))
# 15 What is the character at index 0 in the string Coding For All.
char_0 = company[0]
print('The character at index 0 : ', char_0)
# 16 What is the last index of the string Coding For All.
last_index = len(company) - 1
print('The last index of the string Coding For All is : ', last_index)
# 17 What character is at index 10 in "Coding For All" string.
letter_10 = company[10]
print('The caracter at index 10 : ', letter_10)
# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
based_phrase_18 = 'Python For Everyone'.split(' ')
based_phrase_19 = 'Coding For All'.split(' ')
abbreviation_18 = based_phrase_18[0][0] + based_phrase_18[1][0] + based_phrase_18[2][0]
print('The acronym 18 is : ', abbreviation_18)
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
abbreviation_19 = based_phrase_19[0][0] + based_phrase_19[1][0] + based_phrase_19[2][0]
print('The acronym 19 is : ', abbreviation_19)
# 20 Use index to determine the position of the first occurrence of C in Coding For All.
position_first_occ_of_c = company.index('C') 
print('The position of the first occurence of "C" in Coding For All is : ', position_first_occ_of_c)
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
position_first_occ_of_f = company.index('F')
print('The position of the first occurence of F in Coding For All', position_first_occ_of_f)
# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
sentence_22 = 'Coding For All People'
position_l = sentence_22.rfind('l')
print('The position of the last occr of I is : ', position_l)
# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence_23 = 'You cannot end a sentence with because because because is a conjunction'
first_because_position = sentence_23.find('because')
print('The the position of the first occr of because is : ', first_because_position)
#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_because_position = sentence_23.rindex('because')
print('The position of the last occr of because is : ', last_because_position)
# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_because = sentence_23[first_because_position:last_because_position + len('because')]
print('The because phrase is : ', sentence_because)
# 28 Does 'Coding For All' start with a substring Coding?
sentence_28 = 'Coding For All'
print('Does start with Coding ? : ', sentence_28.startswith('Coding'))
# 29 Does 'Coding For All' end with a substring coding?
print('Does ends with Coding ? : ', sentence_28.endswith('Coding'))
# 30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence_30 = '   Coding For All      '
sentence_without_spaces = sentence_30.strip()
print(sentence_without_spaces)

# 31 Which one of the following variables return True when we use the method isidentifier()
p1 = '30DaysOfPython'
p2 = 'thirty_days_of_python'

print('Is valid variable name : ', p1.isidentifier())
print('Is valid variable name : ', p2.isidentifier())

# 32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib_lists = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_lists = '# '.join(lib_lists)
print('Joined list with hash with space string : ', new_lists)

# 33 Use the new line escape sequence to separate the following sentences.
sentence_33 = 'I am enjoying this challenge\nI just wonder what is next.'
print(sentence_33)

# 34 Use a tab escape sequence to write the following lines.

p34_a = 'Name\tAge\tCountry\tCity'
p34_b = 'Asabeneh\t250\tFinland\tHelsinki'
print(p34_a)
print(p34_b)

# 35 Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2

print(f'''
    radius = {radius}
    area = 3.14 * radius ** 2
    The area of a circle with radius {radius} is {round(area)} meters square.
''')

# 36 Make the following using string formatting methods:
