total = 0
even_count = 0
odd_count = 0

for i in range(1, 11):
    number = int(input(f"Enter number {i}: "))

    if i == 1:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 10

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Total sum: {total}")
print(f"Average: {average}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
