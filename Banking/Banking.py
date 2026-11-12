#This is a banking program

print('---------x--------')
print(f"Banking Program")
balance=0;
def show():
    print(f"Balance Remaining : {balance}")
    print('---------x--------')

def deposit():
    dep=int(input(f"Enter the amount to be deposited : "));
    print('---------x--------')
    return dep;

def withdraw():
    wit=int(input(f"Enter the amount to be withdrawed : "));
    print('---------x--------')
    return wit;

def choice():
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")
    print('---------x--------')


while True:
    print('---------x--------')
    choice()
    choose=int(input(f"Enter your action : "))
    print('---------x--------')
    if(choose<1 or choose>4):
        print("Invalid Action");
    elif(choose==4):
        print("Thank You !!")
        break
    else:
        if(choose==1): 
            show()
        elif(choose==2):
            balance+=deposit()
        else: 
            balance-=withdraw()
            