"""Simple tests for library"""

def test_book_creation():
    from src.library import Book
    book = Book("Test Book", "Test Author")
    assert book.get_title() == "Test Book"
    assert book.author == "Test Author"
    assert book.is_available() == True


def test_library_add():
    from src.library import Book, Library
    library = Library()
    book = Book("Test Book", "Author")
    
    library.add_book(book)
    found = library.find_book("Test Book")
    
    assert found is not None
    assert found.get_title() == "Test Book"


def test_simple():
    assert 1 + 1 == 2
