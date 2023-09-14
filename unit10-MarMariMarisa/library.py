import csv
class Book:
    __slots__ = ["title","author","copies"]
    def __init__(self,title,author,copies):
        self.title = title
        self.author = author
        self.copies = copies

class Patron:
    __slots__ = ["id","name","has","wants"]
    def __init__ (self,id,name):
        self.id = id
        self.name = name
        self.has = []
        self.wants = []

class CardCatalog:
    __slots__ = ["books_by_title","books_by_author"]
    def __init__ (self):
        self.books_by_title = {}
        self.books_by_author = {}

class Library:
    __slots__ = ["patrons","on_shelves","catalog"]
    def __init__(self,filename):
        self.patrons = []
        self.on_shelves = []
        self.catalog = CardCatalog()
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for record in csv_reader:
                title=  record[0]
                author = record[1]
                copies = int(record[2])
                a_book = Book(title,author,copies)
                self.on_shelves.append(a_book)
                #{author: [book1,book2,book3],author2: [book4]}
                if author in self.catalog.books_by_author:
                    self.catalog.books_by_author[author].append(a_book)
                else:
                    self.catalog.books_by_author[author] = [a_book]
                
                books_by_title = self.catalog.books_by_title
                if title in books_by_title:
                    books_by_title[title].append(a_book)
                else:
                    books_by_title[title] = a_book

LIBRARY = Library("data/books.csv")

def find_books_by_author(author):
    if author in LIBRARY.catalog.books_by_author:
        return LIBRARY.catalog.books_by_author[author]
    else:
        return []

def find_books_by_title(title):
    if title in LIBRARY.catalog.books_by_title:
        return LIBRARY.catalog.books_by_author[title]
    else:
        return []

def checkout(book,patron):
    if book.copies > 0 and len(patron.has) < 3:
        patron.has.append(book)
        book.copies -= 1
    else:
        patron.wants.append(book)

def return_book(book,patron):
    #remove book from patron.has
    patron.has.remove(book)
    book.copies += 1
    for patron in LIBRARY.patrons:
        if book in patron.wants:
            patron.wants.remove(book)
            patron.has.append(book)
            book.copies -= 1
            break
    

def main():
    # books = find_books_by_author("George Orwell")
    # for book in books:
    #     print(book.title,",",book.author,",",book.copies)
    # for book in LIBRARY.on_shelves:
    #     print(book.title,",",book.author,",",book.title)

    #     for author in LIBRARY.catalog.books_by_author():
    #         for book in LIBRARY.catalog.books_by_author:
    #             print(author,":",book.title,",",book.author,",",book.copies)
    a_patron = Patron(123,"John Smith")
    book = LIBRARY.on_shelves[0]
    checkout(book,a_patron)
    print(a_patron.has[0].title)
    return_book(book,a_patron)
    print(a_patron.has)
           


if __name__ == "__main__":
    main()
