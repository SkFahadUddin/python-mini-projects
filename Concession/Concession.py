#Concession Program
print("Welcome to the Concession Stand!");
menu={
    "Popcorn": 5.00,
    "Soda": 3.00,
    "Candy": 2.50,
    "Pizza": 8.00,
    "Burger": 6.00,
    "Hot Dog": 4.00,
    "Nachos": 5.50,
    "Water": 1.50
    }
cart=[];
total=0.00;
print(f"Items Available : ");
i=0;
for item, price in menu.items():
    print(f"{i+1}. {item} : ${price:.2f}");
    i+=1;
print(f"Enter the items number to add it to your cart. Type 'done' when you are finished : \n");
while True:
    choice=input("Enter item number or 'done' : ");
    if choice.lower() == "done":
        print(f"Your final cart : ");
        for i in cart:
            print(f"{i}", end=",");
        print(f"Total amount due : ${total:.2f}");
        break;
    elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(menu):
        print("Invalid item number. Please try again.");
        continue;
    else:
        item_number=int(choice);
        item_name=list(menu.keys())[item_number-1];
        cart.append(item_name);
        total+=menu[item_name];
        print(f"Added {item_name} to your cart. Current total: ${total:.2f}");
