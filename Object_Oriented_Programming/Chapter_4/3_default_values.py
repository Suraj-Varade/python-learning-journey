from dataclasses import dataclass, field

@dataclass
class Book:
    # you can define default values.
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = 0.0

b1 = Book()
print(b1) # Book(title='No Title', author='No Author', pages=0, price=0.0)

print("---------------------------------------------------------------------")
## another way to use default - using field function

@dataclass
class Book:
    # you can define default values.
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default = 0.01)
b1 = Book()
print(b1) # Book(title='No Title', author='No Author', pages=0, price=0.01)

# -------------------------------------------------------------------------
print("---------------------------------------------------------------------")

import random

def price_function():
    return float(random.randrange(24, 57))

@dataclass
class Book:
    # you can define default values.
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory= price_function)

b1 = Book()
print(b1) # Book(title='No Title', author='No Author', pages=0, price=40.0)
# Book(title='No Title', author='No Author', pages=0, price=42.0)