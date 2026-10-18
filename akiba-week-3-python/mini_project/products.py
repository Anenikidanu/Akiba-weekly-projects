def add_product(products, name, price, stock):
    name = name.strip()

    if not name:
        return "Product name cannot be empty."

    if search_product(products, name):
        return "Product already exists."

    if price < 0 or stock < 0:
        return "Price and stock cannot be negative."

    products.append({
        "name": name,
        "price": price,
        "stock": stock
    })

    return "Product added successfully."


def search_product(products, name):
    for product in products:
        if product["name"].lower() == name.strip().lower():
            return product

    return None


def update_product(products, name, new_price=None, new_stock=None):
    product = search_product(products, name)

    if product is None:
        return "Product not found."

    if new_price is not None and new_price < 0:
        return "Price cannot be negative."

    if new_stock is not None and new_stock < 0:
        return "Stock cannot be negative."

    if new_price is not None:
        product["price"] = new_price

    if new_stock is not None:
        product["stock"] = new_stock

    return "Product updated successfully."


def display_products(products):
    if not products:
        print("No products available.")
        return

    print("\n--- PRODUCT LIST ---")

    for product in products:
        print(
            f"Name: {product['name']} | "
            f"Price: {product['price']:.2f} Birr | "
            f"Stock: {product['stock']}"
        )