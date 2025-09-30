## equality and comparison

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    

b1 = Book("War and Peace", "Leo", 34.20)
b2 = Book("The Catcher in the rye", "JD", 29.53)
b3 = Book("To kill a mockingBird", "Harper Lee", 24)
b4 = Book("War and Peace", "Leo", 34.20)

## check for equality
print("default comparison : ", b1 == b4) # since both have same values --- False (different memory locations)

# ---------------------------------------------------------------------------------------

## equality and comparison - using __eq__()

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value):
        if isinstance(value, Book):
            return self.title == value.title and self.author == value.author and self.price == value.price    
        else:
            raise ValueError("can't compare")

b1 = Book("War and Peace", "Leo", 34.20)
b2 = Book("The Catcher in the rye", "JD", 29.53)
b3 = Book("To kill a mockingBird", "Harper Lee", 24)
b4 = Book("War and Peace", "Leo", 34.20)

## check for equality
print("comparison after __eq__() custom implementation: ", b1 == b4) # True - since we are implementing __eq__() method 

# ---------------------------------------------------------------------------------------

## greater than equal to comparison.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __ge__(self, value): ## greater than equal
        if isinstance(value, Book):
            return self.price >= value.price    
        else:
            raise ValueError("can't compare")
        
    def __lt__(self, value): ## less than 
        if isinstance(value, Book):
            return self.price < value.price    
        else:
            raise ValueError("can't compare")

b1 = Book("War and Peace", "Leo", 34.20)
b2 = Book("The Catcher in the rye", "JD", 29.53)
b3 = Book("To kill a mockingBird", "Harper Lee", 24)
b4 = Book("War and Peace", "Leo", 34.20)

## check for equality
print(">= comparison __ge__ custom implementation: ", b1 >= b4) 
# >= comparison __ge__ custom implementation:  True

print(">= comparison __ge__ custom implementation: ", b3 >= b4)  # False

# --------------------------------------------------------------------------
## let's sort the book based on their price.

books = [b1,b2,b3,b4]
books.sort() # buit-in - lt operator to sort
print([book.title for book in books])
# ['To kill a mockingBird', 'The Catcher in the rye', 'War and Peace', 'War and Peace']

### want to reverse the order based on price descending 
books.sort(reverse=True)
print([book.title for book in books])
# ['War and Peace', 'War and Peace', 'The Catcher in the rye', 'To kill a mockingBird']