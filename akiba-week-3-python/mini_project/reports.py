def total_revenue(sales):
    total = 0

    for sale in sales:
        total += sale["total"]

    return total


def inventory_value(products):
    total = 0

    for product in products:
        total += product["price"] * product["stock"]

    return total


def low_stock_products(products, threshold=5):
    result = []

    for product in products:
        if product["stock"] < threshold:
            result.append(product)

    return result


def sales_summary(sales):
    print("\n--- SALES SUMMARY ---")

    if not sales:
        print("No sales recorded.")
        return

    for number, sale in enumerate(sales, start=1):
        print(
            f"{number}. {sale['product']} | "
            f"Quantity: {sale['quantity']} | "
            f"Total: {sale['total']:.2f} Birr"
        )

    print(f"Total revenue: {total_revenue(sales):.2f} Birr")


def view_reports(products, sales):
    print("\n========== BUSINESS REPORT ==========")
    print(f"Number of products: {len(products)}")
    print(f"Number of sales: {len(sales)}")
    print(f"Total revenue: {total_revenue(sales):.2f} Birr")
    print(
        f"Remaining inventory value: "
        f"{inventory_value(products):.2f} Birr"
    )

    print("\n--- LOW-STOCK PRODUCTS ---")
    low_stock = low_stock_products(products)

    if low_stock:
        for product in low_stock:
            print(f"{product['name']}: {product['stock']} units")
    else:
        print("No low-stock products.")

    sales_summary(sales)