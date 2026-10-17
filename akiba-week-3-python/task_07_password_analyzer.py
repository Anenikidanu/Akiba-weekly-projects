def check_length(password, minimum_length=8):
    return len(password) >= minimum_length


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digits(password):
    return any(char.isdigit() for char in password)


def check_special_characters(password):
    return any(
        not char.isalnum() and not char.isspace()
        for char in password
    )


def analyze_password(password, minimum_length=8):
    results = {
        "Minimum length": check_length(password, minimum_length),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digits(password),
        "Special character": check_special_characters(password)
    }

    passed = sum(results.values())

    return {
        "requirements": results,
        "passed": passed,
        "total": len(results),
        "all_passed": passed == len(results)
    }


def display_report(password, minimum_length=8):
    report = analyze_password(password, minimum_length)

    print("\n--- PASSWORD REPORT ---")

    for requirement, passed in report["requirements"].items():
        status = "PASS" if passed else "FAIL"
        print(f"{requirement}: {status}")

    print(f"Requirements passed: {report['passed']}/{report['total']}")

    if report["all_passed"]:
        print("All requirements satisfied.")
    else:
        print("Some requirements are missing.")


def main():
    fictional_passwords = [
        "hello",
        "HELLO123!",
        "hello123!",
        "Hello123",
        "Python@2026",
        "Ab1!"
    ]

    print("--- TESTING FICTIONAL PASSWORDS ---")

    for password in fictional_passwords:
        print(f"\nTesting: {password}")
        display_report(password, minimum_length=8)

    # Test a password entered by the user.
    password = input("\nEnter a fictional password to test: ")
    minimum = int(input("Minimum required length (default 8): ") or 8)

    if minimum < 1:
        print("Minimum length must be at least 1.")
    else:
        display_report(password, minimum)


if __name__ == "__main__":
    main()