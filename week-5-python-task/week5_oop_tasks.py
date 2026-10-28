# ==========================
# Task 1: Student Information System
class student:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
    def display_info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Department:",self.department)
st1=student("John",20,"Computer Science")
st2=student("aneni",21,"software engineeering")
st3=student("saba",19,"medicine")
print (" ====================================")
print (" Task 1: Student Information System")
print (" ====================================")
st1.display_info()
st2.display_info()
st3.display_info()
print (" ====================================")
# ==================================
#Task2: Rectangle Calculator
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length*self.width
        print(f"Area : {area}")
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        print(f"Perimeter : {perimeter}")
rect_1=Rectangle(10,20)
rect_2=Rectangle(5,6)
print("Task 2: Rectangle Calculator")
print("=========================================")
rect_1.area()
rect_1.perimeter()
rect_2.area()
rect_2.perimeter()
print (" ====================================") 
# ==================================
#Task 3: Student Score Management

class Student:
    school_name = "Akiba Academy"
    def __init__(self,name,score,department):
        self.name=name
        self.score=score
        self.department=department
    def display(self):
        print("Name : " ,self.name)
        print(f"Score : {self.score}")
        print("Department : " , self.department)
        print("School Name : ",Student.school_name)
stud_1=Student("Nana",90,"nursing")
stud_2=Student("lala",92,"management")
stud_3=Student("santa",88,"civil engineering")
stud_2.score=95    
print("Task 3: Student Score Management")
print("=========================================")
stud_1.display()
stud_2.display()
stud_3.display()
print("=========================================")
# ==================================
#Task 4: Product Information System
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return (
        f"Name: {self.name}\n"
        f"Price: {self.price}\n"
        f"Quantity: {self.quantity}"
    )
    def total_value(self):
        total=self.price*self.quantity
        return total
prod_1=Product("napkin",100,10)
prod_2=Product("choclate",200,5)
prod_3=Product("dresses",900,4)
print("Task 4: Product Information System")
print("=========================================")
print(prod_1)
print(f"Total Value : {prod_1.total_value()} \n" )
print(prod_2)
print(f"Total Value : {prod_2.total_value()} \n" )
print(prod_3)
print(f"Total Value : {prod_3.total_value()} \n" )
print("=========================================")
#Task 5: Bank Account Management
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount):
         if amount <= 0:
            print("Withdrawal amount must be positive")
         elif amount > self.balance:
            print("Insufficient funds")
         else:
            self.balance -= amount
        
    def display_balance(self):
        return( f"Owner: {self.owner}\n"
               f"Balance: {self.balance}")
print("Task 5: Bank Account Management")
print("=========================================")
acc_1=BankAccount("tutu",1000)
acc_1.deposit(500)
acc_1.withdraw(300)
acc_1.withdraw(2000)
acc_2=BankAccount("semdal",5000)
acc_2.deposit(-4000)
acc_2.withdraw(1000)
acc_2.deposit(200)
print(acc_1.display_balance())
print(acc_2.display_balance())
print("=========================================")