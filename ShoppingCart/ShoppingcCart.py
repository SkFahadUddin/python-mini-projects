# Shopping cart
items = ["Apple", "Banana", "Orange", "Grapes", "Mango",
         "Watermelon", "Pineapple", "Strawberry", "Blueberry", "Raspberry"]
cart = {}

while True:
    print("\n1. Add item  2. Remove item  3. View cart  4. Checkout  5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        for number, name in enumerate(items, start=1):
            print(f"{number}. {name}")
        try:
            number = int(input("Item number to add: "))
            quantity = int(input("Quantity: "))
            if not 1 <= number <= len(items) or quantity <= 0:
                print("Invalid item number or quantity.")
                continue
            name = items[number - 1]
            cart[name] = cart.get(name, 0) + quantity
            print(f"Added {quantity} {name}(s).")
        except ValueError:
            print("Enter numbers only.")

    elif choice == "2":
        if not cart:
            print("Cart is empty.")
            continue
        for number, (name, quantity) in enumerate(cart.items(), start=1):
            print(f"{number}. {name} (quantity: {quantity})")
        try:
            number = int(input("Cart item number to remove: "))
            if not 1 <= number <= len(cart):
                print("Invalid item number.")
                continue
            name = list(cart)[number - 1]
            del cart[name]
            print(f"Removed {name}.")
        except (ValueError, IndexError):
            print("Invalid item number.")

    elif choice in ("3", "4"):
        if not cart:
            print("Cart is empty.")
        else:
            print("Your cart:")
            for name, quantity in cart.items():
                print(f"{name}: {quantity}")
            print(f"Total items: {sum(cart.values())}")
        if choice == "4":
            print("Checkout complete.")
            break

    elif choice == "5":
        break
    else:
        print("Invalid option.")
