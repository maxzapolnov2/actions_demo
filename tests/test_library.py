"""Tests for library management system"""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from actions_demo.library import Book, PrintedBook, EBook, User, Librarian, Library


def test_book_creation():
    """Test Book class creation"""
    book = Book("Test Book", "Test Author", 2023, True)
    assert book.get_title() == "Test Book"
    assert book.get_author() == "Test Author"
    assert book.get_year() == 2023
    assert book.is_available()


def test_book_availability():
    """Test book availability methods"""
    book = Book("Test Book", "Test Author", 2023, True)
    book.mark_as_taken()
    assert not book.is_available()
    book.mark_as_returned()
    assert book.is_available()


def test_printed_book():
    """Test PrintedBook class"""
    pbook = PrintedBook("Printed Book", "Author", 2020, 300, "хорошая")
    assert pbook.get_title() == "Printed Book"
    assert pbook.pages == 300
    assert pbook.condition == "хорошая"


def test_ebook():
    """Test EBook class"""
    ebook = EBook("EBook", "Author", 2021, 5, "epub")
    assert ebook.get_title() == "EBook"
    assert ebook.file_size == 5
    assert ebook.format == "epub"


def test_user_borrow_return():
    """Test User borrow/return functionality"""
    user = User("Test User")
    book = Book("Test Book", "Author", 2023, True)

    user.borrow(book)
    borrowed_books = user.get_borrowed_books()
    assert len(borrowed_books) == 1
    assert borrowed_books[0].get_title() == "Test Book"

    user.return_book(book)
    assert len(user.get_borrowed_books()) == 0


def test_library_operations():
    """Test Library basic operations"""
    library = Library()
    book = Book("Test Book", "Author", 2023, True)
    user = User("Test User")

    # Add book and user
    library.add_book(book)
    library.add_user(user)

    # Lend book
    library.lend_book("Test Book", "Test User")
    assert not book.is_available()
    assert len(user.get_borrowed_books()) == 1

    # Return book
    library.return_book("Test Book", "Test User")
    assert book.is_available()
    assert len(user.get_borrowed_books()) == 0


def test_librarian():
    """Test Librarian functionality"""
    library = Library()
    librarian = Librarian("Library Admin")
    book = Book("Test Book", "Author", 2023, True)
    user = User("Regular User")

    librarian.add_book(library, book)
    librarian.register_user(library, user)

    assert library.find_book("Test Book") is not None


def test_printed_book_repair():
    """Test PrintedBook repair method"""
    pbook = PrintedBook("Old Book", "Author", 1990, 200, "плохая")
    pbook.repair()
    assert pbook.condition == "хорошая"

    pbook.repair()
    assert pbook.condition == "новая"


def test_simple():
    """Simple test to verify setup works"""
    assert 1 + 1 == 2
