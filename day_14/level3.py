# level3
# Use the countries_data.py
# (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py)
# file and follow the tasks below: 
# - Sort countries by name, by capital, by population -
# Sort out the ten most spoken languages by location. 
# - Sort out the ten most populated countries.
from countries_data import countries

print(sorted(countries, key=lambda c: c['name']))
print(sorted(countries, key=lambda c: c['capital']))
print(sorted(countries, key=lambda c: c['population']))

# Ten most spoken languages by location

# Ten most populated countries

'''
Task: the ten most populated countries

This is the same sort by population, plus two things you already used:

Sort by population with reverse=True, so the biggest comes first.
Take the first ten with a slice, like [:10] (you did this in #14).

Then, if you want a cleaner result, keep only the names, using a list comprehension or map.

Task: the ten most spoken languages by location

This one is harder, so here is what it means.

“Most spoken languages by location” means: which languages appear in the most countries. Each country has a languages list, for example ["English", "French"]. You count how many countries list each language, then keep the ten with the highest counts.

The expected result looks like this (language and number of countries):

English  -> appears in many countries
French   -> appears in many countries
Arabic   -> ...

Plan, step by step

Collect all languages from all countries into one flat list. This is the flattening idea from Day 13: a nested loop or comprehension over country['languages'] for each country.
Count each language. Use a dictionary, like your create_dict_from_list in #13: counts[lang] = counts.get(lang, 0) + 1.
Sort the counts, largest first. A dictionary has items as (language, count) pairs, so sorted(counts.items(), key=lambda pair: pair[1], reverse=True) sorts them by the count (the second item).
Take the first ten with [:10].

Tips

Test steps 1 and 2 on a small list of three or four countries before using the full data.
Print after each step to see what you have.
If you used collections.Counter, the most_common(10) method does steps 2 to 4, but the dictionary way is good practice for now.
'''
