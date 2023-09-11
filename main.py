class Book:
    def __init__(self, title, author, genre, **kwargs):
        self.title = title
        self.author = author
        self.genre = genre
        self.borrower = None
        self.details = kwargs

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, genre={self.genre})>"
    

class Library:
    def __init__(self):
        self.books = set()

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.add(book)

    def borrow_book(self, title, borrower):
        for book in self.books:
            if book.title == title and book.borrower is None:
                book.borrower = borrower
                return f"{title} has been borrowed by {borrower}."
        return f"{title} is either not in the library or is already borrowed."

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.borrower:
                book.borrower = None
                return f"{title} has been returned."
        return f"{title} wasn't borrowed."
    def __iter__(self):
        self._iter_books = iter(self.books)
        return self
    
    def __next_(self):
        return(self._iter_books)
    
    def borrowed_books(self):
        return (book for book in self.books if book.borrower is not None)
    
    def add_multiple_books(self, *args):
        for book in args:
            self.add_book(book)

    