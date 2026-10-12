correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("PIN verified successfully!")
        break
    else:
        print("Incorrect PIN.")

        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
        else:
            print("ATM locked. Too many incorrect attempts.")
