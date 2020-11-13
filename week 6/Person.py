from dataclasses import dataclass, field
from typing import List
import csv


@dataclass
class Product:
    name: str
    price: float

@dataclass
class ProductStock:
    product: Product
    quantity: int

@dataclass
class Shop:
    cash: float = 0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str
    budget: float = 0.0
    shopping_list: List[ProductStock] = field(default_factory=list)

def create_and_stock_shop():
    s = Shop()
    with open('stock.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            p = Product(row[0], float(row[1]))
            ps = ProductStock(p, float(row[2]))
            s.stock.append(ps)
            # print(ps)
    return s

def print_product(p):
    print(f'\nProduct name: {p.name} \n Product price: {p.price}')

def print_customer(c):
    print(f'Customer name: {c.name} \n Customer budget: {c.budget}')

    for item in c.shopping_list:
        print_product(item.product)

        print(f'{c.name} Orders {item.quantity} of above product')
        cost = item.quantity * item.product.price

        print(f'The cost to {c.name} will be {cost}Euro')

def print_shop(s):
    print(f'Shop has {s.cash} in cash')

    for item in s.stock:
        print_product(item.product)

        print(f'The shop has {item.quantity} of the above')

# p = Product()
s = create_and_stock_shop()
print_shop(s)