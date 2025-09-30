from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __repr__(self):
        return f"customized : {self.title} by {self.author} total pages : {self.pages}, cost : {self.price}"

    def __call__(self, price):
        self.price = price

    ## overriding __post_init__() function, let us customized additional properties
    # after the object has been initialized via built-in __init__()
    def __post_init__(self):
        self.desc = f"automated description... added"

b1 = Book("2 State", "chetan bhagat", 324, 20)
print(b1) 
## before override of __repr__()
# Book(title='2 State', author='chetan bhagat', pages=324, price=20)
## after override of __repr__()
# customized : 2 State by chetan bhagat, total pages : 324, cost : 20

b1(24.56)
print(b1) # customized : 2 State by chetan bhagat, total pages : 324, cost : 24.56

b1(120)
print(b1)

print(b1.desc) # automated description... added