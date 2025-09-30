class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, price, publisher , period):
        super().__init__(title, price, publisher, period)


class Newspaper(Periodical):
    def __init__(self, title, price, publisher , period):
        super().__init__(title, price, publisher, period)
        

b1 = Book("Brave new world", "aldous Huxley", 311, 29.0)
n1 = Newspaper("Ny Times", 6.0, "New york times company", "Daily")
m1 = Magazine("Scientific American", 5.99, "Springer Nature", "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
'''
aldous Huxley
New york times company
29.0 5.99 6.0
'''