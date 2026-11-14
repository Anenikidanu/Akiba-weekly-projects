class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if self.search_book(book.isbn):
            print("A book with this ISBN already exists.")
            return

        self.books.append(book)
        print("Book added successfully!")

    def remove_book(self, isbn):
        book = self.search_book(isbn)

        if book is None:
            print("Book not found.")
            return

        if not book.is_available:
            print("Cannot remove a borrowed book.")
            return

        self.books.remove(book)
        print("Book removed successfully!")

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book

        return None

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return

        for book in self.books:
            book.display_info()
            print("----------------------------")
