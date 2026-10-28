
# Week 4 Mini-Project: Student Marks Manager
# Demonstrating mutability, references, identity, and copying.


def main():
    # Step 1: Create the original list with five student marks.
    original_marks = [75, 80, 65, 90, 85]

    # Step 2: Create a shared reference to the original list.
    shared_reference = original_marks

    # Step 3: Create an independent copy of the original list.
    copied_marks = original_marks.copy()

    # Compare the original and copied lists before modifying the copy.
    print("Before modifying the copy:")
    print(
        "Original and copied lists have equal values:",
        original_marks == copied_marks
    )
    print(
        "Original and copied lists are identical:",
        original_marks is copied_marks
    )

    # Step 4: Add a new mark to the copied list only.
    copied_marks.append(95)

    # Step 5: Display all three lists.
    print("\nOriginal marks:", original_marks)
    print("Shared reference:", shared_reference)
    print("Copied marks:", copied_marks)

    # Step 6: Compare the lists using identity and equality.
    print(
        "\nOriginal and shared reference are identical:",
        original_marks is shared_reference
    )

    print(
        "Original and copied lists have equal values:",
        original_marks == copied_marks
    )

    print(
        "Original and copied lists are identical:",
        original_marks is copied_marks
    )


if __name__ == "__main__":
    main()
