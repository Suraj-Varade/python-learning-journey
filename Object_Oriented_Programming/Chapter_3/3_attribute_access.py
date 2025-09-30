class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, cost: {self.price}"
    
    def __getattribute__(self, name): 
        # called when an attr is retrieved, don't 
        # directly access the attr name otherwise a recursive loop is created.
        if name and name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("value must be a float.")
        return super().__setattr__(name, value)
    
    def __getattr__(self, name):
        return name + " is not here !!!"
    
b1 = Book("War and Peace", "Leo", 34.20)
b2 = Book("The Catcher in the rye", "JD", 29.53)
b3 = Book("To kill a mockingBird", "Harper Lee", 24.34)
b4 = Book("War and Peace", "Leo", 34.20)

print(b4) # War and Peace by Leo, cost: 34.2

b4.price = 100.34
print(b4) # War and Peace by Leo, cost: 90.306

## let me try setting a integer value for price.
b2.price = 22.34
print(b2) 
'''
Traceback (most recent call last):
  File "/Users/surajvarade/Personal/Programs/Python/Object_Oriented_Programming/Chapter_3/3_attribute_access.py", line 37, in <module>
    b2.price = 22
    ^^^^^^^^
  File "/Users/surajvarade/Personal/Programs/Python/Object_Oriented_Programming/Chapter_3/3_attribute_access.py", line 23, in __setattr__
    raise ValueError("value must be a float.")
ValueError: value must be a float.
'''