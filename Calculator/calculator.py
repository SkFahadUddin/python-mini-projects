# A calculator
print(f"This is a calculator");
print(f"1.Addition  2.Subtraction   3.Multiplication    4.Division");
operation=int(input("Write the specific number to perform the operation between two numbers : "));
if(operation<1 or operation>4):
    print(f"Invalid operation");
else:
    num1=int(input(f"Enter the first number : "));
    num2=int(input(f"Enter the second number : "));

    if(operation==1):
        print(f"The result of addition is : {num1+num2}");
    elif(operation==2):
        print(f"The result of subtraction is : {num1-num2}");
    elif(operation==3):
        print(f"The result of multiplication is : {num1*num2}");
    elif(operation==4):
        print(f"The result of division is : {num1/num2}");