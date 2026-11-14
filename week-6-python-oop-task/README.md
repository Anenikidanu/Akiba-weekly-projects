# Week: 6 Topic: Object-Oriented Programming (OOP)


## Student Information

- **Name:** Aneni Kidanu
- **GitHub Username:** anenikidanu
- **Assignment:** Week 6 Python Task
- **Organization:** Akiba Technologies

---

## 1. Project Description

This assignment demonstrates the application of Object-Oriented Programming (OOP) concepts using Python.

It consists of two practical exercises. The first implements a Product and ShoppingCart system to demonstrate different types of methods and object relationships. The second develops a menu-driven Library Management System to demonstrate how OOP principles can be used to organize and manage a real-world application.

## 2. OOP Concepts Demonstrated

The assignment demonstrates the following concepts:

- **Classes and Objects:** Used to create and manage entities such as products, books, libraries, and members.
- **Constructors:** The `__init__()` method initializes object attributes.
- **Instance Attributes:** Store individual object data.
- **Class Attributes:** Store shared data across instances.
- **Instance Methods:** Perform operations on individual objects.
- **Class Methods:** Modify or access class-level attributes.
- **Static Methods:** Perform independent operations related to a class.
- **Encapsulation:** Restricts direct access to internal object attributes.
- **Inheritance:** Allows child classes to reuse attributes and methods from parent classes.
- **Polymorphism:** Allows different classes to provide different implementations of the same method.
- **Method Overriding:** Allows child classes to redefine inherited methods.
- **super():** Provides access to parent class methods and constructors.
- **Composition:** Allows objects to contain and manage other objects.

## 3. Project Structure

```text
OOP_Assignment/
│
├── questions
│   ├── question_1.py
│   ├──question_2.py
|   ├──question_3.py
|   ├──question_4.py
|   ├──question_5.py
├── mini_project/
│   ├── main.py
│   ├── book.py
│   ├── library.py
│   └── member.py
│
└── README.md
```

## 4. Instructions for Running the Programs

### Requirements

- Python 3 installed on your computer.
- A code editor such as Visual Studio Code.

### Running Question 5

Navigate to the question_5 directory and run:

```bash
python product.py
```

### Running the Library Management System

Navigate to the mini_project directory and run:

```bash
python main.py
```

The Library Management System provides a menu-driven interface that allows users to add, search, display, and remove books, register members, and manage borrowing and returning operations.

## 5. Mini-Project Explanation: Library Management System

### Project Objective

The Library Management System is a simple Python application developed using Object-Oriented Programming principles. Its purpose is to manage library books and registered members while controlling the borrowing and returning process.

### Class Descriptions

**1. Book Class**

The Book class represents individual books in the library. It stores the book title, author, ISBN, and availability status. It also provides methods to display book information and update availability.

**2. Library Class**

The Library class manages a collection of Book objects. It provides methods for adding, removing, displaying, and searching for books using their ISBN.

**3. Member Class**

The Member class represents registered library members. It stores member information and a collection of borrowed books. It provides methods for borrowing and returning books while checking availability and borrowing limits.

**4. StudentMember Class**

StudentMember inherits from the Member class. It overrides the borrowing-limit method to allow students to borrow a maximum of two books.

**5. TeacherMember Class**

TeacherMember also inherits from the Member class. It overrides the borrowing-limit method to allow teachers to borrow a maximum of five books.

### OOP Implementation in the Mini-Project

- **Inheritance:** StudentMember and TeacherMember inherit from Member.
- **Encapsulation:** Book availability is managed through a private attribute and controlled methods.
- **Polymorphism:** Different member types provide different borrowing limits through the overridden method.
- **Method Overriding:** Both child classes redefine the get_borrowing_limit() method.
- **super():** Child class constructors use super() to initialize attributes inherited from Member.
- **Composition:** Library maintains a collection of Book objects, while members maintain their borrowed books.

### Program Functionality

The application supports the following operations:

1. Add a new book.
2. Display all books.
3. Search for a book using ISBN.
4. Register student and teacher members.
5. Borrow books.
6. Return borrowed books.
7. Exit the application.

The system prevents members from borrowing unavailable books, exceeding their borrowing limits, or returning books they have not borrowed.

## 6. Conclusion

This assignment provided practical experience in applying Object-Oriented Programming concepts to real-world problems. By implementing the Product and ShoppingCart system and the Library Management System, I gained a better understanding of how classes, objects, inheritance, encapsulation, polymorphism, and composition work together.

OOP makes software easier to organize, maintain, reuse, and extend. These principles are especially important when developing larger software applications.
