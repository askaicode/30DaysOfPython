# Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'Test', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Middle skill
if 'skills' in person:
    skills = person['skills']
    n = len(skills)
    mid = n // 2
    if n % 2 == 0:
        print('The middle skills:', skills[mid - 1:mid + 1])
    else:
        print('The middle skill:', skills[mid])

# 2. Does the person have Python?
if 'skills' in person:
    if 'Python' in person['skills']:
        print('The person has the Python skill')
    else:
        print('The person does not have the Python skill')

# 3. Developer title
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print('He is a backend developer')
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. Married and lives in Finland
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")