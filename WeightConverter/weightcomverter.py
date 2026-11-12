# A weight converter
print(f"This is a weight converter");
print(f"1.Kilograms to Pounds  2.Pounds to Kilograms");
operation=int(input("Write the specific number to perform the operation : "));
if(operation<1 or operation>4):
    print(f"Invalid operation");
else:
    weight=int(input(f"Enter the weight : "));

    if(operation==1):
        print(f"{weight} Kilograms is {weight * 2.20462:.2f} Pounds");
    elif(operation==2):
        print(f"{weight} Pounds is {weight / 2.20462:.2f} Kilograms");