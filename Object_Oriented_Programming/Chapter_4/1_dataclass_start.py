from dataclasses import dataclass
## once you declare the dataclass, we probably don't need to specify __init__() method, 
# dataclass is managing that for us

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def book_info(self):
        return f"{self.title} by {self.author}"
    

b1 = Book("New World", "Jia Jang", 1200, 34.98)
b2 = Book("The catcher int the Rye", "JD", 322, 29.45)
b3 = Book("New World", "Jia Jang", 1200, 34.98)
print(b1) # use repr - built-in
print(b2) # use repr - built-in
'''
Book(title='New World', author='Jia Jang', pages=1200, price=34.98)
Book(title='The catcher int the Rye', author='JD', pages=322, price=29.45)
'''

print(b1 == b3) # True (automatically implements - __eq__(), attr value based)
print(b1 == b2) # False

b1.title = "Anna Karenina"
b1.pages = 2345
print(b1.book_info()) ## Anna Karenina by Jia Jang