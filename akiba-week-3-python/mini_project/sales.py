def record_sale(products, sales, name, quantity):
    from products import search_product

    product = search_product(products, name)

    if product is None:
        return None, "Product not found."

    if quantity <= 0:
        return None, "Quantity must be positive."

    if quantity > product["stock"]:
        return None, "Insufficient stock."

    sale = {
        "product": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total": product["price"] * quantity
    }

    product["stock"] -= quantity
    sales.append(sale)

    return sale, "Sale recorded successfully."


def generate_receipt(sale):
    print("\n========== AKIBA RECEIPT ==========")
    print(f"Product: {sale['product']}")
    print(f"Quantity: {sale['quantity']}")
    print(f"Unit price: {sale['unit_price']:.2f} Birr")
    print("-----------------------------------")
    print(f"Total cost: {sale['total']:.2f} Birr")
    print("===================================")