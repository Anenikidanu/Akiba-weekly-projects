class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = True

    @property
    def is_available(self):
        return self.__is_available

    def update_availability(self, status):
        self.__is_available = status

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {status}")
