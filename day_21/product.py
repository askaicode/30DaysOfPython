from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1
    
    def total_price(self):
        return self.price * self.quantity


class ProductNormal:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity


p = Product('Notebook', 2.5, 10)
print(p)
print(p.total_price())

p2 = Product('Pen', 1.2)
print(p2.quantity)

a = Product('Pen', 1.2, 5)
b = Product('Pen', 1.2, 5)
print(a == b) # true

pn = ProductNormal('Pencil', 2.5, 4)
pn2 = ProductNormal('Pencil', 2.5, 4)
print(pn == pn2) # False

cart = [
    Product('Notebook', 2.5, 10),
    Product('Pen', 1.2, 5),
    Product('Bag', 20, 1)
]