from products import (
    add_product,
    search_product,
    update_product,
    display_products
)

from sales import record_sale, generate_receipt

from reports import view_reports


def get_number(prompt, number_type=float):
    try:
        return number_type(input(prompt))
    except ValueError:
        print("Invalid input. Enter a valid number.")
        return None


def main():
    products = []
    sales = []

    while True:
        print("\n===== AKIBA BUSINESS TOOLKIT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Record Sale")
        print("6. View Reports")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Product name: ")
            price = get_number("Price: ")
            stock = get_number("Initial stock: ", int)

            if price is None or stock is None:
                continue

            print(add_product(products, name, price, stock))

        elif choice == "2":
            display_products(products)

        elif choice == "3":
            name = input("Product name to search: ")
            product = search_product(products, name)

            if product:
                print(product)
            else:
                print("Product not found.")

        elif choice == "4":
            name = input("Product name to update: ")
            product = search_product(products, name)

            if product is None:
                print("Product not found.")
                continue

            print("1. Update price")
            print("2. Update stock")
            print("3. Update both")

            option = input("Choose an option: ")

            if option not in ("1", "2", "3"):
                print("Invalid option.")
                continue

            price = None
            stock = None

            if option in ("1", "3"):
                price = get_number("New price: ")

                if price is None:
                    continue

            if option in ("2", "3"):
                stock = get_number("New stock: ", int)

                if stock is None:
                    continue

            print(update_product(products, name, price, stock))

        elif choice == "5":
            name = input("Product sold: ")
            quantity = get_number("Quantity sold: ", int)

            if quantity is None:
                continue

            sale, message = record_sale(
                products, sales, name, quantity
            )

            print(message)

            if sale is not None:
                generate_receipt(sale)

        elif choice == "6":
            view_reports(products, sales)

        elif choice == "7":
            print("Thank you for using Akiba Business Toolkit!")
            break

        else:
            print("Invalid option. Choose from 1 to 7.")


if __name__ == "__main__":
    main()