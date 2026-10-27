# 1. Create an empty tuple
empty_tuple = ()

# 2. Create tuples of brothers and sisters
brothers = ('Twist', 'Doal', 'Jimmy')
sisters = ('Talescia', 'Julie', 'Elodie')

# 3. Join them and assign to siblings
siblings = brothers + sisters

# 4. How many siblings?
print('Number of siblings:', len(siblings))

# 5. Add father and mother -> family_members
parents = ('Gabriel', 'Marie')
family_members = siblings + parents
print(family_members)