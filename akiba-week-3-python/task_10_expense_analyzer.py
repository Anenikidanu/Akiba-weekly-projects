def add_expense(expenses, description, category, amount):
    description = description.strip()
    category = category.strip()

    if not description or not category:
        return "Description and category cannot be empty."

    if amount <= 0:
        return "Expense amount must be positive."

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

    return "Expense added successfully."


def calculate_total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def spending_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in categories:
            categories[category] = 0

        categories[category] += amount

    return categories


def find_largest_expense(expenses):
    if not expenses:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above_threshold(expenses, threshold=200):
    result = []

    for expense in expenses:
        if expense["amount"] > threshold:
            result.append(expense)

    return result


def highest_spending_category(expenses):
    categories = spending_by_category(expenses)

    if not categories:
        return None

    highest = max(categories, key=categories.get)

    return highest, categories[highest]


def generate_report(expenses, threshold=200):
    total = calculate_total_expenses(expenses)
    categories = spending_by_category(expenses)

    print("\n--- EXPENSE REPORT ---")
    print(f"Total expenses: {total:.2f} Birr")

    print("\nSpending by category:")

    for category, amount in categories.items():
        percentage = (amount / total * 100) if total else 0
        print(f"{category}: {amount:.2f} Birr ({percentage:.2f}%)")

    largest = find_largest_expense(expenses)

    print("\nLargest expense:")
    print(largest if largest else "No expenses recorded.")

    print(f"\nExpenses above {threshold:.2f} Birr:")

    above_threshold = expenses_above_threshold(expenses, threshold)

    if above_threshold:
        for expense in above_threshold:
            print(expense)
    else:
        print("None")

    highest = highest_spending_category(expenses)

    print("\nHighest-spending category:")
    print(highest if highest else "No expenses recorded.")


def main():
    expenses = [
        {"description": "Lunch", "category": "Food", "amount": 180},
        {"description": "Taxi", "category": "Transport", "amount": 120},
        {"description": "Groceries", "category": "Food", "amount": 450},
        {"description": "Internet", "category": "Bills", "amount": 300}
    ]

    while True:
        print("\n--- EXPENSE MENU ---")
        print("1. Add expense")
        print("2. View report")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Description: ")
            category = input("Category: ")

            try:
                amount = float(input("Amount: "))
                print(add_expense(
                    expenses, description, category, amount
                ))
            except ValueError:
                print("Enter a valid amount.")

        elif choice == "2":
            try:
                threshold = float(
                    input("Threshold (default 200): ") or 200
                )

                if threshold < 0:
                    print("Threshold cannot be negative.")
                else:
                    generate_report(expenses, threshold)

            except ValueError:
                print("Enter a valid threshold.")

        elif choice == "3":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()