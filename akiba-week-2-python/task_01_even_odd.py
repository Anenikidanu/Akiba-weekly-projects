num=int(input(" enter a number :"))
reminder=num%2
if reminder==0 :
    print(f" {num} is even")
else :
    print (f"{num} is odd")
if num<0:
    print(f"{num} is negative number ")
elif num>0:
    print(f"{num} is positive number")
else :
    print (f"{num} is Zero")