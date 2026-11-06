sales = [
    {'product': 'Bread', 'price': 2},
    {'product': 'Milk',  'price': 3},
    {'product': 'Bread', 'price': 2},
    {'product': 'Juice', 'price': 4},
    {'product': 'Bread', 'price': 2},
    {'product': 'Milk',  'price': 3},
]

# How many times each product was sold
count = {}
for sale in sales:
    name = sale['product']
    count[name] = count.get(name, 0) + 1
print(count)

# How much money each product made
money = {}
for sale in sales:
    name = sale['product']
    money[name] = money.get(name, 0) + sale['price']
print(money)
pairs = []
for name in money:
    pairs.append((money[name], name))
pairs.sort(reverse=True)
print(pairs[:2])