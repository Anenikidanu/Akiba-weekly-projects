# Theory Answers

## Question 1: Function Design

A function containing 100 lines of code to manage products, process sales, and generate reports can become difficult to maintain because it performs too many different tasks in one place. If a problem occurs, finding and fixing it can take more time. Changing one part of the program may also affect other parts.

### 1. Single-purpose functions

A function should ideally perform one main task. This makes the program easier to understand and organize.

For example, product management, sales processing, and report generation should be handled by separate functions instead of one large function.

### 2. Parameters and return values

Parameters allow a function to receive the data it needs. Return values allow it to send results back to the part of the program that called it.

This makes functions more flexible because they can work with different data instead of depending on fixed values.
def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(50, 3)
print(total)  # 150


Here, the function receives the price and quantity as parameters and returns the calculated total.

### 3. Code reuse

Reusable functions allow developers to write code once and call it whenever needed. This reduces repetition and makes updates easier.

For example, a `search_product()` function can be used when updating a product, recording a sale, or searching for a product.

### 4. Testing and debugging

Small functions are easier to test because each function has a specific responsibility. If a calculation produces an incorrect result, the developer can test that function separately instead of examining a large block of code.

### 5. Dividing the program into smaller functions

I would divide the program according to its responsibilities:

- `add_product()` to add a new product.
- `search_product()` to find a product.
- `update_product()` to modify product information.
- `record_sale()` to process a sale and update stock.
- `calculate_revenue()` to calculate total sales revenue.
- `generate_report()` to display business information.

Each function would receive the required data through parameters and return its result when appropriate.

### Poorly organized example

def manage_business():
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    total = price * quantity

    print("Product:", name)
    print("Total:", total)

This function collects input, performs a calculation, and displays the result in one place. It is not necessarily incorrect, but combining these responsibilities makes the code less reusable and harder to test independently.

### Improved example

def calculate_total(price, quantity):
    return price * quantity


def display_product(name, total):
    print("Product:", name)
    print("Total:", total)


name = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = calculate_total(price, quantity)
display_product(name, total)

In the improved version, calculating the total and displaying the product information are separate tasks. The calculation function can be reused elsewhere and tested without asking for user input.

In conclusion, dividing a large function into smaller, single-purpose functions improves readability, code reuse, testing, debugging, and maintenance.

---

## Question 2: Mutable Data and Function Side Effects

Consider the following code:
def add_item(items, item):
    items.append(item)
    return items


products = ["Pen", "Book"]
result = add_item(products, "Bag")

print(products)
print(result)

Output:
['Pen', 'Book', 'Bag']
['Pen', 'Book', 'Bag']

### 1. Why both printed results contain the added item

Both results contain `"Bag"` because the function modifies the original list using `items.append(item)`.

The variable `items` refers to the same list object as `products`. The variable `result` also refers to that same list because the function returns `items`.

Therefore, all three variables refer to the same list object.

### 2. How lists behave when passed to functions

Lists are mutable, meaning their contents can be changed after they are created.

When a list is passed to a function, the parameter refers to the same list object. If the function modifies that list using methods such as `append()`, `remove()`, or `clear()`, the changes can be seen outside the function.

For example:
def add_item(items, item):
    items.append(item)


products = ["Pen", "Book"]

add_item(products, "Bag")

print(products)
Output:


['Pen', 'Book', 'Bag']

Even though the function does not return anything, the original list changes because the function modifies the existing list object.

### 3. Modifying an existing list versus returning a new list

Modifying an existing list changes the object that already exists. Returning a new list creates a separate list object, leaving the original list unchanged.

For example, using `append()` modifies the existing list:
products = ["Pen", "Book"]
products.append("Bag")

print(products)

Output:
['Pen', 'Book', 'Bag']

To avoid modifying the original list, we can create a new list using the `+` operator:
def add_item(items, item):
    new_items = items + [item]
    return new_items


products = ["Pen", "Book"]
result = add_item(products, "Bag")

print(products)
print(result)

Output:
['Pen', 'Book']
['Pen', 'Book', 'Bag']

In this example, `items + [item]` creates a new list. The original `products` list remains unchanged, while `result` refers to the new list.

### 4. When modifying the original data is useful and when it may cause problems

Modifying the original list is useful when the program needs to update shared data directly. For example, an inventory system may need to reduce a product's stock after a successful sale.
def sell_product(product, quantity):
    if quantity <= product["stock"] and quantity > 0:
        product["stock"] -= quantity
        return True

    return False

The product dictionary is modified directly, so the updated stock is available to other parts of the program that use the same dictionary.

However, modifying original data can cause unexpected problems when other parts of the program rely on the previous values. For example, a function may accidentally remove an item from a list that another function also uses.

Returning a new list can be safer when the original data needs to be preserved, such as when creating a filtered list or preparing a modified copy for comparison.

In conclusion, mutable lists allow functions to modify shared data, which can be useful for updating information. However, developers should understand these side effects and choose whether to modify the original object or return a new one based on the program's requirements.
