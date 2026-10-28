
# Week 4 Python Task
# Mutability, References, and Memory Model in Python


def question_1():
    print("\n===== QUESTION 1: MUTABLE AND IMMUTABLE OBJECTS =====")

    # Lists are mutable, so their elements can be changed.
    numbers = [10, 20, 30]
    numbers[0] = 100

    print("Modified list:", numbers)

    # Strings are immutable. Concatenation creates a new string.
    text = "Hello"
    text = text + " World"

    print("Modified string:", text)


def question_2():
    print("\n===== QUESTION 2: REFERENCES AND OBJECT IDENTITY =====")

    a = [10, 20, 30]
    b = a
    c = [10, 20, 30]

    print(a is b)
    print(a is c)
    print(a == c)

    # is checks identity; == checks equality.


def question_3():
    print("\n===== QUESTION 3: SHARED REFERENCES =====")

    # Both variables refer to the same list.
    numbers = [1, 2, 3]
    values = numbers

    values.append(4)

    print("Original numbers:", numbers)
    print("Values:", values)

    # Create a separate list using copy().
    numbers = [1, 2, 3]
    values = numbers.copy()
    values.append(4)

    print("\nOriginal numbers after copying:", numbers)
    print("Independent values:", values)


def question_4():
    print("\n===== QUESTION 4: FUNCTION ARGUMENTS =====")

    # This function modifies the original list.
    def update_list_original(items):
        items.append(100)

    scores = [50, 60, 70]
    update_list_original(scores)

    print("Original function result:", scores)

    # This function creates and returns a new list.
    def update_list(items):
        new_items = items.copy()
        new_items.append(100)
        return new_items

    scores = [50, 60, 70]
    updated_scores = update_list(scores)

    print("Original scores:", scores)
    print("Updated scores:", updated_scores)


def question_5():
    print("\n===== QUESTION 5: MEMORY MANAGEMENT =====")

    numbers = [10, 20, 30]
    values = numbers

    print("Before deleting numbers:")
    print("numbers:", numbers)
    print("values:", values)

    # Delete the variable name numbers.
    # The list remains accessible through values.
    del numbers

    print("\nAfter deleting numbers:")
    print("values:", values)


if __name__ == "__main__":
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
