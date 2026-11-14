class Product:
    store_name = "Akiba Store"

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Store: {self.store_name}")

   
    @classmethod
    def change_store_name(cls, new_name):
        cls.store_name = new_name

    @staticmethod
    def is_valid_price(price):
        return price > 0
class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def display_cart(self):
        print("\n========== SHOPPING CART ==========")

        for product in self.products:
            product.display_product()

        print(f"Total: {self.calculate_total()}")
# Creating products
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)
p3 = Product("Keyboard", 2500)

# Checking prices
print(Product.is_valid_price(p1.price))  # True

# Creating shopping cart
cart = ShoppingCart()

# Adding products
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

# Displaying cart
cart.display_cart()

# Changing store name
Product.change_store_name("Akiba Tech Store")

# Displaying updated store name
p1.display_product()