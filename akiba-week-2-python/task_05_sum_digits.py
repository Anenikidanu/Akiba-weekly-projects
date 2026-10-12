number = int(input("Enter a positive number: "))

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number //= 10

print(f"Sum of digits: {total}")
