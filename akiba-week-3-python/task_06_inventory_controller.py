def add_product(inventory, name, price, stock):
    name = name.strip()

    if not name:
        return "Product name cannot be empty."

    if name.lower() in inventory:
        return "Product already exists."

    if price < 0 or stock < 0:
        return "Price and stock cannot be negative."

    inventory[name.lower()] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    return "Product added successfully."


def search_product(inventory, name):
    return inventory.get(name.strip().lower())


def update_price(inventory, name, new_price):
    product = search_product(inventory, name)

    if product is None:
        return "Product not found."

    if new_price < 0:
        return "Price cannot be negative."

    product["price"] = new_price
    return "Price updated successfully."


def increase_stock(inventory, name, quantity):
    product = search_product(inventory, name)

    if product is None:
        return "Product not found."

    if quantity <= 0:
        return "Quantity must be positive."

    product["stock"] += quantity
    return "Stock increased successfully."


def sell_product(inventory, name, quantity):
    product = search_product(inventory, name)

    if product is None:
        return "Product not found."

    if quantity <= 0:
        return "Quantity must be positive."

    if quantity > product["stock"]:
        return "Insufficient stock."

    product["stock"] -= quantity
    total = product["price"] * quantity

    return f"Sale successful. Total: {total:.2f} Birr"


def total_inventory_value(inventory):
    total = 0

    for product in inventory.values():
        total += product["price"] * product["stock"]

    return total


def low_stock_report(inventory, threshold=5):
    print(f"\n--- LOW STOCK (Below {threshold}) ---")

    found = False

    for product in inventory.values():
        if product["stock"] < threshold:
            print(product)
            found = True

    if not found:
        print("No low-stock products.")


def main():
    inventory = {}

    while True:
        print("\n--- INVENTORY MENU ---")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price")
        print("4. Increase stock")
        print("5. Sell product")
        print("6. View all products")
        print("7. Total inventory value")
        print("8. Low-stock report")
        print("9. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                name = input("Product name: ")
                price = float(input("Price: "))
                stock = int(input("Stock quantity: "))
                print(add_product(inventory, name, price, stock))

            elif choice == "2":
                name = input("Product name: ")
                print(search_product(inventory, name) or "Product not found.")

            elif choice == "3":
                name = input("Product name: ")
                price = float(input("New price: "))
                print(update_price(inventory, name, price))

            elif choice == "4":
                name = input("Product name: ")
                quantity = int(input("Quantity to add: "))
                print(increase_stock(inventory, name, quantity))

            elif choice == "5":
                name = input("Product name: ")
                quantity = int(input("Quantity to sell: "))
                print(sell_product(inventory, name, quantity))

            elif choice == "6":
                for product in inventory.values():
                    print(product)

                if not inventory:
                    print("Inventory is empty.")

            elif choice == "7":
                print(
                    f"Inventory value: "
                    f"{total_inventory_value(inventory):.2f} Birr"
                )

            elif choice == "8":
                threshold = int(input("Low-stock threshold: "))
                if threshold < 0:
                    print("Threshold cannot be negative.")
                else:
                    low_stock_report(inventory, threshold)

            elif choice == "9":
                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Invalid input. Enter the correct number format.")


if __name__ == "__main__":
    main()