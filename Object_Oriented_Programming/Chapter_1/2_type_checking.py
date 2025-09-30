class Book:
    def __init__(self, title):
        self.title = title

class NewsPaper:
    def __init__(self, title):
        self.title = title        

## checking type
b1 = Book("System Design")
b2 = Book("DSA")
n1 = NewsPaper("TOI")
n2 = NewsPaper("Lokmat")

print(type(b1)) # <class '__main__.Book'>
print(type(n1)) # <class '__main__.NewsPaper'>

## compare two types together
print(b1 == b2) # False
print(type(b1) == type(b2)) # True

## use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book)) # True
print(isinstance(n1, NewsPaper)) # True
print(isinstance(b1, NewsPaper)) # False

print(isinstance(b1, object)) # True -- everything in python, is an instance of a generic built in object class 