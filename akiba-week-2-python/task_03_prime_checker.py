num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not prime")
else:
    is_prime = True
    # We only need to check up to the square root of the number.
    # If a number has a divisor larger than its square root,
    # it must also have a corresponding divisor smaller than the square root.
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")