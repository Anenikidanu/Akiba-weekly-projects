class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print("Manager Information")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    
    def display_info(self):
        print("Developer Information")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Programming Language:", self.programming_language)


employee1 = Employee("Abebe", 30000)
manager1 = Manager("Sara", 50000, "IT")
developer1 = Developer("Dawit", 40000, "Python")

employee1.display_info()

print()

manager1.display_info()

print()

developer1.display_info()