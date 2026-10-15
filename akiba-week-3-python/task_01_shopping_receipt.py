def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        if item['price'] < 0 or item['quantity'] < 0:
            raise ValueError("Price and quantity must be non-negative.")

        subtotal += item['price'] * item['quantity']

    return subtotal


def calculate_discount(subtotal):
    if subtotal < 1000:
        discount = 0
    elif subtotal < 3000:
        discount = subtotal * 0.05
    else:
        discount = subtotal * 0.10

    return discount


def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1.")

    return amount * tax_rate


def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    total_after_discount = subtotal - discount
    tax = calculate_tax(total_after_discount, tax_rate)
    total = total_after_discount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "total_after_discount": total_after_discount,
        "tax": tax,
        "total": total
    }
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]
receipt = generate_receipt(items, 0.15)
print("===== SHOPPING RECEIPT =====")

for item in items:
    print(f"{item['name']} x {item['quantity']}: "
          f"{item['price'] * item['quantity']:.2f} Birr")

print("----------------------------")
print(f"Subtotal:             {receipt['subtotal']:.2f} Birr")
print(f"Discount:             {receipt['discount']:.2f} Birr")
print(f"After discount:       {receipt['total_after_discount']:.2f} Birr")
print(f"Tax:                  {receipt['tax']:.2f} Birr")
print("----------------------------")
print(f"FINAL AMOUNT:         {receipt['total']:.2f} Birr")
print("============================")
