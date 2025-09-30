class Book:
    # static properties, defined at the class level are shared by all instances.
    BOOK_TYPES = ("HARDCOVER", "PAPERBAG", "EBOOK")

    def __init__(self, title, book_type):
        self.title = title
        if book_type and self.BOOK_TYPES.__contains__(book_type):
            self.book_type = book_type
        else:
            self.book_type = None

    # double underscore properties are hidden from other classes
    __booklist = None

    # create a static method
    def getbooklist():
        if(Book.__booklist == None):
            Book.__booklist = []
        return Book.__booklist

    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    def set_title(self, newtitle):
        self.title = newtitle

    def print_book_info(self):
        print(f"Book Info => ", f"title : {self.title}", f"\nbook_type ; ", self.book_type if self.book_type else "Not Found")
        
b1 = Book("THE WORLD", None)
b1.print_book_info()
'''
Book Info =>  title : THE WORLD 
book_type ;  Not Found
'''

b2 = Book("THE WORLD", "EBOOK")
b2.print_book_info()
'''
Book Info =>  title : THE WORLD 
book_type ;  EBOOK
'''

b3 = Book("THE WORLD", "Unknown")
b3.print_book_info()
'''
Book Info =>  title : THE WORLD 
book_type ;  Not Found
'''

print(b3.BOOK_TYPES) # ('HARDCOVER', 'PAPERBAG', 'EBOOK')

print(b3.get_book_types())
print(Book.get_book_types())

# use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b3)

for b in thebooks:
    print(b.title)
