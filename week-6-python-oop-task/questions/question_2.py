
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += amount
            print(f"Successfully deposited {amount} ETB.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew {amount} ETB.")

    def get_balance(self):
        print(f"Current balance: {self.__balance} ETB.")

account1 = BankAccount("Ani", 5000)
account2 = BankAccount("Abel", 3000)

print("\n Account 1 ")
print("Account Holder:", account1.account_holder)

account1.deposit(1000)
account1.withdraw(2000)
account1.get_balance()

print("\n Account 2 ")
print("Account Holder:", account2.account_holder)

account2.deposit(500)
account2.withdraw(1000)
account2.get_balance()

print("\n Invalid Transactions ")
account1.deposit(-500)
account2.withdraw(5000)

print("\n Final Balances ")
account1.get_balance()
account2.get_balance()
