"""Tests for library"""
from actions_demo.library import Book, Library


def test_book_creation():
    book = Book("Test Book")
    assert book.get_title() == "Test Book"
    assert book.is_available() is True


def test_library_add_book():
    library = Library()
    book = Book("Test Book")
    library.add_book(book)
    found = library.find_book("Test Book")
    assert found is not None
    assert found.get_title() == "Test Book"


def test_simple():
    assert 1 + 1 == 2
