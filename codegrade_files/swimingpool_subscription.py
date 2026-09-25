def validate_float(input_str: str) -> bool:
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def validate_int(input_str: str) -> bool:
    try:
        int(input_str)
        return True
    except ValueError:
        return False


subscription_str = input("Enter subscription: ")
single_price_str = input("Enter single price: ")
visits_str = input("Enter number of visits: ")

if not validate_float(subscription_str) or not validate_float(single_price_str) or not validate_int(visits_str):
    print("Invalid input")
else:
    subscription = float(subscription_str)
    single_price = float(single_price_str)
    visits = int(visits_str)

    total_single = single_price * visits

    print(f"Single tickets: €{total_single}")
    print(f"Monthly subscription: €{subscription}")

    if total_single <= subscription:
        print("Advice: Buy single tickets")
    else:
        print("Advice: Buy a subscription")
        savings = total_single - subscription
        print(f"You save €{savings}")
