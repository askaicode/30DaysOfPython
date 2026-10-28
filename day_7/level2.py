
# Level 2 

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
A_union_B = A.union(B)
print('A join B : ', A_union_B)

# 2. Find A intersection B
A_inter_B = A & B # or A.intersection(B)
print('A intersection B : ', A_inter_B)

# 3. Is A subset of B
print('Is A subset of B : ', A.issubset(B))

# 4. Are A and B disjoint sets
print('Are A and B disjoint sets : ', A.isdisjoint(B))

# 5. Joint A with B and B with A
AB = A.union(B) # A | B
BA = B.union(A) # B | A

print('Are they equal ? : ', AB == BA)

# 6. The symmetric difference between A and B
symmetric_diff = A.symmetric_difference(B) # A^B
print('The symmetric difference between A and B is : ', symmetric_diff)

# 7. Delete the sets completely
del A, B
try:
    print(A, B)
except NameError:
    print('A and B has been deleted')