# create a basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret_book_token = "AB12344"
    
    # create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self, amount):
        self._discount = amount
    

# create an instance
b1 = Book("Brave New World", "Leo Tolstroy", 1225, 39.95)
b2 = Book("War and Peace", "JD", 230, 29.95)

# print the class and property
# print(b1) # <__main__.Book object at 0x102b3ea50>
print(b1.title) # Brave New World
b1.setdiscount(0.25)
print(b1.getprice())
print(b1._Book__secret_book_token) # AB12344
