class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def get_borrowing_limit(self):
        return 0

    def borrow_book(self, book):
        if book is None:
            print("Book not found.")
            return

        if not book.is_available:
            print("This book is already borrowed.")
            return

        if len(self.borrowed_books) >= self.get_borrowing_limit():
            print("You have reached your borrowing limit.")
            return

        book.update_availability(False)
        self.borrowed_books.append(book)

        print(f"{self.name} borrowed '{book.title}' successfully!")

    def return_book(self, book):
        if book not in self.borrowed_books:
            print("You did not borrow this book.")
            return

        self.borrowed_books.remove(book)
        book.update_availability(True)

        print(f"{self.name} returned '{book.title}' successfully!")


class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 2


class TeacherMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 5
