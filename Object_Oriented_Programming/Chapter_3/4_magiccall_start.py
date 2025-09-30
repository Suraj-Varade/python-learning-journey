class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, cost: {self.price}"
    
    def __call__(self, title, author, price): 
        ## __call__ method can be used to call the object like a function
        self.title = title
        self.author = author
        self.price = price
    
b1 = Book("War and Peace", "Leo", 34.20)
b2 = Book("The Catcher in the rye", "JD", 29.53)
print(b1) # War and Peace by Leo, cost: 34.2
print(b2) # The Catcher in the rye by JD, cost: 29.53

b1("anna karenina", "leo", 324.23) # anna karenina by leo, cost: 324.23
print(b1)