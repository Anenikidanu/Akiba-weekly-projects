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