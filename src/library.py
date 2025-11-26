class Book:
    def __init__(self, title, author, year, available):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = available

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False
    
    def mark_as_returned(self):
        self.__available = True


class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year, True)
        self.pages = pages
        self.condition = condition
    
    def repair(self):
        con_list = ["новая", "хорошая", "плохая"]
        if (self.condition in con_list) and (self.condition != "новая"):
            self.condition = con_list[con_list.index(self.condition)-1]


class EBook(Book):
    def __init__(self, title, author, year, file_size, format):
        super().__init__(title, author, year, True)
        self.file_size = file_size
        self.format = format
    
    def download(self):
        print('Загрузка началась!')


class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []
    
    def borrow(self, book):
        self.__borrowed_books.append(book)

    def return_book(self, book):
        self.__borrowed_books.remove(book)

    def show_books(self):
        for b in self.__borrowed_books:
            print(b.get_title())

    def get_borrowed_books(self):
        return self.__borrowed_books.copy()


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
    def remove_book(self, library, title):
        library.remove_book(title)
    def register_user(self, library, user):
        library.add_user(user)

class Library:
    def __init__(self):
       self.__books = []
       self.__users = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                self.__books.remove(book)
                break

    def add_user(self, user):
        self.__users.append(user)
        
    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def show_all_books(self):
        print(self.__books)

    def show_available_books(self):
        to_show = []
        for book in self.__books:
            if book.is_available():
                to_show.append(book)
        print(to_show)

    def lend_book(self, title, user_name):
        user = None
        for u in self.__users:
            if u.name == user_name:
                user = u
                break
        
        book = self.find_book(title)
        
        if user and book:
            user.borrow(book)
            book.mark_as_taken()

    def return_book(self, title, user_name):
        user = None
        for u in self.__users:
            if u.name == user_name:
                user = u
                break
        
        book = self.find_book(title)
        
        if user and book:
            user.return_book(book)
            book.mark_as_returned()

if __name__ == '__main__':
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)
    
    user1.show_books()
    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    # --- пользователь смотрит свои книги ---
    user1.show_books()

    # --- возвращает книгу ---
    lib.return_book("Война и мир", "Анна")

    user1.show_books()
    # --- электронная книга ---
    b2.download()

    # --- ремонт книги ---
    b3.repair()
    print(b3.condition)
