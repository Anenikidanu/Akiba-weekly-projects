first_num=int(input(" enter the first number :"))
second_num=int(input(" enter the second number :"))
third_num=int(input(" enter the third number :"))
if first_num==second_num==third_num:
    print("All the numbers are equal")
elif first_num==second_num:
    if first_num>third_num:
        print(f"{first_num} and {second_num} are equal and larger than {third_num}")
    else :
        print (f"{third_num} is the largest of all three")
elif first_num==third_num:
    if first_num>second_num:
        print(f"{first_num} and {third_num} are equal and larger than {second_num}")
    else :
        print (f"{second_num} is the largest of all three")
elif third_num==second_num:
    if third_num>first_num:
        print(f"{third_num} and {second_num} are equal and larger than {first_num}")
    else :
        print (f"{first_num} is the largest of all three")
elif first_num>second_num:
    if first_num>third_num:
        print (f"{first_num} is the largest of all three")
    else :
        print(f"{third_num} is the largest of all three")
elif  second_num>third_num:
        print(f"{second_num} is the largest of all three")
else:
    print (f"{third_num} is the largest of all three")
