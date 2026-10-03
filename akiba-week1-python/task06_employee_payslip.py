emp_name = input("Employee Name : ")
basic_sal = float(input("Basic Salary : "))
trans_allowance = float(input("Transport Allowance : "))
food_allowance = float(input("Food Allowance : "))

gross_sal = basic_sal + trans_allowance + food_allowance

print("=====================================")
print("\tEMPLOYEE PAYSLIP")
print("=====================================")
print("Employee : " + emp_name)
print(f"Basic Salary : \t {basic_sal} ETB")
print(f"Transport Allowance : \t {trans_allowance} ETB")
print(f"Food Allowance : \t {food_allowance} ETB")
print("--------------------------------------")
print(f"Gross Salary : \t {gross_sal} ETB")
print("=====================================")