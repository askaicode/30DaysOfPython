data = [
    {"name": "Finland", "population": 5},
    {"name": "Albania", "population": 3},
    {"name": "Chad", "population": 14},
]

# Answer with key
def get_name(country):
    return country['name']

print(sorted(data, key=lambda c: c['name'], reverse=True))