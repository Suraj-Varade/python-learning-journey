class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # use of __str__ returns a string.
    def __str__(self):
        return f"Book info => title : {self.title}\nauthor: {self.author}\nprice:{self.price}"
    
    # use the __repr___ method to return an object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("New World", "Jia Jang", 34.98)
print(b1)
'''
Book info => title : New World
author: Jia Jang
price:34.98
'''

print(str(b1))
'''
Book info => title : New World
author: Jia Jang
price:34.98
'''

print(repr(b1))
'''
title=New World, author=Jia Jang, price=34.98
'''
