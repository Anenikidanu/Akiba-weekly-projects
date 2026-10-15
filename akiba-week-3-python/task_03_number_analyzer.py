def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def get_divisors(number):
    if number == 0:
        raise ValueError("Zero has infinitely many divisors.")

    divisors = []

    for divisor in range(1, abs(number) + 1):
        if abs(number) % divisor == 0:
            divisors.append(divisor)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return reversed_number * sign


def analyze_number(number):
    if number == 0:
        divisors = "Undefined: zero has infinitely many divisors."
    else:
        divisors = get_divisors(number)

    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return {
        "number": number,
        "parity": parity,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": divisors
    }


# Test the program
number = int(input("Enter an integer: "))

result = analyze_number(number)

print("\n===== NUMBER ANALYSIS =====")

for key, value in result.items():
    print(f"{key}: {value}")
