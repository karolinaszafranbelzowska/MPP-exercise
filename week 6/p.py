
  
from dataclasses import dataclass,field
import csv
from typing import List

@dataclass
class Product:
    name: str
    price: float =0.0

@dataclass
class ProductStock:
    product: Product
    quantity: int

@dataclass
class Shop:
    cash: float =0.0
    stock: List[ProductStock] = field(default_factory=list)

@dataclass
class Customer:
    name: str
    budget: float
    shopping_list: List[ProductStock] = field(default_factory=list)


def create_and_stock_shop():
    s= Shop()
    with open('stock.csv') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        line_count=0
        first_row= next(csv_reader)
        s.cash=float(first_row[0])
        for row in csv_reader:
            p= Product(row[0],float(row[1]))
            ps= ProductStock(p,float(row[2]))
            s.stock.append(ps)
            #print(ps)
    return s
def read_customer(file_path):
    with open(file_path) as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        first_row= next(csv_reader)
        c = Customer(first_row[0], float(first_row[1]))
        print(c)
        for row in csv_reader:
            name=row[0]
            quantity = float(row[1])
            p=Product(name)
            ps=ProductStock(p,quantity)
            c.shopping_list.append(ps)
        return c

def print_product(p):
    print(f'\n Product Name: {p.name} \n Product Price:{p.price}')

def print_customer(c):
    print(f'\n Customer Name: {c.name} \n Customer Budget:{c.budget}')

    for items in c.shopping_list:
        print_product(items.product)

        print(f'{c.name} Orders {items.quantity} of above product')
        cost=items.quantity*items.product.price
        print(f'the cost to {c.name} is ${cost}')
def print_shop(s):
    print(f'Shop has{s.cash} in cash')
    for item in s.stock:
        print_product(item.product)
        print(f'The item have {item.quantity} in stock' )
    
p= Product("COke",1.0)
#s=create_and_stock_shop()
#print_shop(s)
c= read_customer("../customer.csv")
print_customer(c)
