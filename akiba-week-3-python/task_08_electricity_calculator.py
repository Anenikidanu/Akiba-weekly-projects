def validate_units(units):
    return units >= 0


def calculate_tier_charges(units):
    if not validate_units(units):
        raise ValueError("Units cannot be negative.")

    first_tier = min(units, 50) * 0.50

    second_tier = min(max(units - 50, 0), 100) * 0.75

    third_tier = max(units - 150, 0) * 1.20

    return {
        "first_tier": first_tier,
        "second_tier": second_tier,
        "third_tier": third_tier
    }


def calculate_total_bill(units, service_fee=0):
    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    charges = calculate_tier_charges(units)

    energy_charge = sum(charges.values())

    return energy_charge + service_fee


def generate_billing_summary(units, service_fee=0):
    charges = calculate_tier_charges(units)
    total = calculate_total_bill(units, service_fee)

    print("\n--- ELECTRICITY BILL ---")
    print(f"Units consumed: {units}")
    print(f"First 50 units: {charges['first_tier']:.2f} Birr")
    print(f"Next 100 units: {charges['second_tier']:.2f} Birr")
    print(f"Above 150 units: {charges['third_tier']:.2f} Birr")
    print(f"Service fee: {service_fee:.2f} Birr")
    print(f"Total bill: {total:.2f} Birr")


def main():
    try:
        units = float(input("Enter units consumed: "))
        service_fee = float(input("Enter service fee (0 if none): "))

        if not validate_units(units):
            print("Units cannot be negative.")
        elif service_fee < 0:
            print("Service fee cannot be negative.")
        else:
            generate_billing_summary(units, service_fee)

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()