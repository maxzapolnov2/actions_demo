"""Library management system"""


class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def get_title(self):
        return self.title

    def is_available(self):
        return self.available


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                return book
        return None
