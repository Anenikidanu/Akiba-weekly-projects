def record_transaction(history, transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    history.append(transaction)


def deposit(balance, amount, history):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance

    balance += amount
    record_transaction(history, "deposit", amount, balance)

    print("Deposit successful.")
    return balance


def withdraw(balance, amount, history, daily_total, daily_limit):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance, daily_total

    if amount > balance:
        print("Insufficient balance.")
        return balance, daily_total

    if daily_total + amount > daily_limit:
        print("Daily withdrawal limit exceeded.")
        return balance, daily_total

    balance -= amount
    daily_total += amount

    record_transaction(history, "withdrawal", amount, balance)

    print("Withdrawal successful.")
    return balance, daily_total


def check_balance(balance):
    print(f"Current balance: {balance:.2f} Birr")


def transaction_summary(history, opening_balance, balance):
    total_deposited = 0
    total_withdrawn = 0

    for transaction in history:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        else:
            total_withdrawn += transaction["amount"]

    print("\n--- TRANSACTION SUMMARY ---")
    print(f"Opening balance: {opening_balance:.2f} Birr")
    print(f"Total deposited: {total_deposited:.2f} Birr")
    print(f"Total withdrawn: {total_withdrawn:.2f} Birr")
    print(f"Final balance: {balance:.2f} Birr")

    print("\nTransaction history:")

    if not history:
        print("No transactions recorded.")

    for transaction in history:
        print(transaction)


def main():
    opening_balance = float(input("Opening balance: "))
    daily_limit = float(input("Daily withdrawal limit: "))

    if opening_balance < 0 or daily_limit < 0:
        print("Balances and limits cannot be negative.")
        return

    balance = opening_balance
    daily_total = 0
    history = []

    while True:
        print("\n--- BANK MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Transaction summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice in ("1", "2"):
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Enter a valid number.")
                continue

            if choice == "1":
                balance = deposit(balance, amount, history)
            else:
                balance, daily_total = withdraw(
                    balance, amount, history,
                    daily_total, daily_limit
                )

        elif choice == "3":
            check_balance(balance)

        elif choice == "4":
            transaction_summary(history, opening_balance, balance)

        elif choice == "5":
            transaction_summary(history, opening_balance, balance)
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()