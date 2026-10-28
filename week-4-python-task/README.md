# Week 4 Python Task: Mutability, References, and Memory Model in Python

## Student Information

- **Name:** Aneni Kidanu
- **GitHub Username:** anenikidanu
- **Assignment:** Week 4 Python Task
- **Organization:** Akiba Technologies

---

# Question 1: Mutable and Immutable Objects

## Explanation

Mutable objects are objects whose contents can be changed after they have been created. Examples include lists, dictionaries, and sets.

Immutable objects are objects whose values cannot be changed in place after creation. Examples include strings, integers, floats, and tuples.

For example, a list allows us to change an element directly, while a string does not allow us to change one of its characters directly. When we perform an operation such as string concatenation, Python creates a new string object.

## Program Output

```text
Modified list: [100, 20, 30]
Modified string: Hello World
```

## Output Explanation

The list initially contains `[10, 20, 30]`. When the first element is changed to `100`, the original list is modified because lists are mutable.

The original string is `"Hello"`. Concatenating `" World"` creates a new string, `"Hello World"`, and assigning it to the variable `text` makes the variable refer to the new string. The original string object is not modified.

---

# Question 2: References and Object Identity

## Program Output

```text
True
False
True
```

## Answers

### 1. What is the output?

The program prints `True`, `False`, and `True` on separate lines.

### 2. Explain the difference between `is` and `==`.

The `is` operator checks whether two variables refer to the same object in memory. The `==` operator checks whether two objects have equal values.

For example, `a is b` is `True` because both variables refer to the same list. However, `a is c` is `False` because `c` refers to a separate list. The expression `a == c` is `True` because both lists contain the same elements.

### 3. Why do `a` and `c` have the same values but different identities?

The variable `a` is assigned a list containing `[10, 20, 30]`. The variable `c` is assigned a new list containing the same elements. Although the lists have equal contents, they are separate objects in memory. Therefore, `a == c` is `True`, while `a is c` is `False`.

---

# Question 3: Shared References and Side Effects

## Program Output

```text
Original numbers: [1, 2, 3, 4]
Values: [1, 2, 3, 4]

Original numbers after copying: [1, 2, 3]
Independent values: [1, 2, 3, 4]
```

## Answers

### 1. Predict the output.

The original program prints `[1, 2, 3, 4]` twice because `numbers` and `values` refer to the same list. Appending `4` through `values` changes the shared list.

### 2. Explain why modifying `values` also affects `numbers`.

The statement `values = numbers` does not create a new list. Instead, it creates another reference to the same list object. When `values.append(4)` is executed, the shared object is modified, so both variables show the updated list.

### 3. Rewrite the code so modifying `values` does not change `numbers`.

The statement `values = numbers.copy()` creates a separate list containing the same elements. Appending an element to this new list does not change the original list.

---

# Question 4: Function Arguments and Mutability

## Program Output

```text
Original scores: [50, 60, 70]
Updated scores: [50, 60, 70, 100]
```

## Answers

### 1. What is the output?

The original function appends `100` to the list passed to it. The original example therefore prints `[50, 60, 70, 100]`.

In the corrected program, the function creates and returns a new list. The original scores remain `[50, 60, 70]`, while the updated scores become `[50, 60, 70, 100]`.

### 2. Explain why the original list changes after the function call.

The list `scores` is passed to the function `update_list()`. The parameter `items` refers to the same list object. Since lists are mutable, appending `100` through `items` changes the original list.

### 3. Modify the function so that it creates and returns a new list without changing the original list.

The function can use `items.copy()` to create an independent list, append `100` to the copy, and return it. The original list remains unchanged because the function modifies the new list instead of the original object.

---

# Question 5: Memory Management and Garbage Collection

## Explanation

Python manages objects in memory automatically. When an object is created, Python allocates memory for it and variables can hold references to that object.

Python uses reference counting in CPython to track references to objects. It also has a garbage collector that can detect and clean up reference cycles that reference counting alone cannot reclaim.

The `del` statement removes a reference, such as a variable name. It does not necessarily destroy the object immediately because other variables may still refer to it.

When an object is no longer reachable through any usable references, it becomes eligible for memory reclamation. The exact time at which memory is reclaimed depends on the Python implementation.

## Program Output

```text
Before deleting numbers:
numbers: [10, 20, 30]
values: [10, 20, 30]

After deleting numbers:
values: [10, 20, 30]
```

## Answers

### 1. What happens when `del` is used?

The `del` statement removes the specified variable name or reference. In this example, `del numbers` removes the name `numbers` from the current scope.

### 2. Does deleting one variable always destroy the object?

No. Deleting one variable does not necessarily destroy the object. If another variable still refers to that object, the object remains accessible through that variable.

### 3. What happens when an object is no longer referenced?

When an object is no longer reachable through any usable references, it can be reclaimed by Python's memory management system. In CPython, reference counting often reclaims ordinary objects promptly, while the garbage collector handles reference cycles. Other Python implementations may reclaim memory at different times.

---

# Practical Mini-Project: Student Marks Manager

## Project Description

The Student Marks Manager demonstrates mutable objects, shared references, independent copies, object identity, and equality. The program creates a list of student marks, assigns the list to another variable, and creates an independent copy. It then adds a new mark to the copy and compares the lists using `is` and `==`.

## Program Output

```text
Original marks: [75, 80, 65, 90, 85]
Shared reference: [75, 80, 65, 90, 85]
Copied marks: [75, 80, 65, 90, 85, 95]

Original and shared reference are identical: True
Original and copied lists have equal values: False
Original and copied lists are identical: False

Before modifying the copy:
Original and copied lists have equal values: True
Original and copied lists are identical: False
```

## Project Reflection

### 1. Why does modifying a shared reference affect the original list?

Modifying a shared reference affects the original list because both variables refer to the same list object in memory. Any changes made through either variable modify that shared object.

### 2. Why does modifying the copied list not affect the original list?

Modifying the copied list does not affect the original because the copy is a separate list object. The two lists initially contain the same values, but changes to one list do not change the other list.

### 3. What is the difference between equality and identity in Python?

Equality checks whether two objects have equal values, while identity checks whether two references point to the exact same object. The `==` operator checks equality, and the `is` operator checks identity.

---

# How to Run the Programs

## Requirements

- Python 3 installed on the computer.
- The three assignment files saved in the same folder.

## Running the assignment questions

Open a terminal in the project folder and execute:

```bash
python questions.py
```

## Running the Student Marks Manager

Execute:

```bash
python student_marks_manager.py
```

On Windows, if the `python` command is unavailable, use `py` instead.

---

# What I Learned

Through this assignment, I learned the difference between mutable and immutable objects in Python. I also learned how variables refer to objects, how `is` differs from `==`, and how shared references can cause side effects when modifying mutable objects.

I practised creating independent copies of lists, passing mutable objects to functions, and returning new lists without changing the originals. Finally, I learned how `del`, object references, reference counting, and garbage collection relate to Python memory management.

The Student Marks Manager helped me apply these concepts in a practical program.