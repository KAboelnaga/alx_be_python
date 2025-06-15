class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False
    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.books:
            if book.title == title and not book.checked_out:
                book.checked_out = True
                print(f"You have checked out: {book}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self.books:
            if book.title == title and book.checked_out:
                book.checked_out = False
                print(f"You have returned: {book}")
                return
        print(f"Book '{title}' was not checked out.")
    def __str__(self):
        return f"{self.title} by {self.author}"
class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_available_books(self):
        """List all available books in the library."""
        for book in self.books:
            if not book.checked_out:
                print(book)

    