import library

def test_book():
    a_book = library.Book("ABC Book", "John Smith", 5)
    assert a_book.title == "ABC Book"
    assert a_book.author == "John Smith"
    assert a_book.copies == 5

def test_patron():
    a_patron = library.Patron(123,"Tom")
    assert a_patron.id == 123
    assert a_patron.has == []
    assert a_patron.name == "Tom"
    assert a_patron.wants == []
    a_book = library.Book("ABC Book","John Smith")

def test_catalog():
    a_catalog = library.CardCatalog()
    assert a_catalog.books_by_author == {}
    assert a_catalog.books_by_title == {}
