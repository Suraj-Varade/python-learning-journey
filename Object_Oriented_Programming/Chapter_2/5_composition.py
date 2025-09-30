## has a - relation

class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price
        self.chapters = []
        self.author = author

    def add_chapter(self, chapter = None):
        if chapter:
            self.chapters.append(chapter)

    def get_page_count(self):
        result = 0
        for chapter in self.chapters:
            result += chapter.pages
        return result


class Author:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Chapter:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages


auth = Author("Leo", "Tolstroy")
b1 = Book("War and Peace",29.45, auth)
chapter1 = Chapter("chapter1", 23)
chapter2 = Chapter("chapter2", 33)
chapter3 = Chapter("chapter3", 63)
b1.add_chapter(chapter1)
b1.add_chapter(chapter2)
b1.add_chapter(chapter3)

print(f"title : {b1.title}, author : {auth.firstname}, totalChapters : {len(b1.chapters)}")
# title : War and Peace, author : Leo, totalChapters : 3
print(f"Total pages =>> {b1.get_page_count()}") # Total pages =>> 119

