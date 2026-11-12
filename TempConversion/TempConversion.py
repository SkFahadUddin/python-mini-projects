#Temperature Conversion
print(f"This is a temperature converter");
print(f"1. Celsius to Fahrenheit  2. Fahrenheit to Celsius");
operation=int(input("Enter the specific number to perform the operation : "));
if(operation<1 or operation>4):
    print(f"Invalid operation");
else:
    temp=int(input(f"Enter the temperature : "));

    if(operation==1):
        print(f"{temp} Celsius is {temp * 9.0/5.0 +32.0 :.2f} Fahrenheit");
    elif(operation==2):
        print(f"{temp} Fahrenheit is {(temp - 32.0) * 5.0/9.0 :.2f} Celsius");