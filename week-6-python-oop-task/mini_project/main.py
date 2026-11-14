from book import Book
from library import Library
from member import StudentMember, TeacherMember

def main():
    library = Library()
    members = []

    while True:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # 1. Add Book
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")

            book = Book(title, author, isbn)
            library.add_book(book)

        # 2. Display All Books
        elif choice == "2":
            library.display_books()

        # 3. Search Book
        elif choice == "3":
            isbn = input("Enter ISBN: ")
            book = library.search_book(isbn)

            if book:
                book.display_info()
            else:
                print("Book not found.")

        # 4. Register Member
        elif choice == "4":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")

            existing_member = next(
                (m for m in members if m.member_id == member_id),
                None
            )

            if existing_member:
                print("Member ID already exists.")
                continue

            print("\n1. Student Member")
            print("2. Teacher Member")

            member_type = input("Choose member type: ")

            if member_type == "1":
                member = StudentMember(name, member_id)

            elif member_type == "2":
                member = TeacherMember(name, member_id)

            else:
                print("Invalid member type.")
                continue

            members.append(member)
            print("Member registered successfully!")

        # 5. Borrow Book
        elif choice == "5":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")

            member = next(
                (m for m in members if m.member_id == member_id),
                None
            )

            book = library.search_book(isbn)

            if member is None:
                print("Member not found.")
            else:
                member.borrow_book(book)

        # 6. Return Book
        elif choice == "6":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")

            member = next(
                (m for m in members if m.member_id == member_id),
                None
            )

            book = library.search_book(isbn)

            if member is None:
                print("Member not found.")
            elif book is None:
                print("Book not found.")
            else:
                member.return_book(book)
        elif choice == "7":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
