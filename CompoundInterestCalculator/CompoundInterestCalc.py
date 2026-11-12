#Compound Interest Calculator
print(f"This is a compound interest calculator");
pamt=int(input(f"Enter the principal amount : $"));
if(pamt<0 or pamt>1000000):
    print(f"Invalid principal amount");
else:
        r=float(input(f"Enter the rate of interest : "));
        if(r<0 or r>100):
            print(f"Invalid rate of interest");
        else:
            t=int(input(f"Enter the time have passed in years : "));
            if(t<0 or t>100):
                print(f"Invalid time");
            else:
                a=pamt*pow(1+r/100,t);
                print(f"The compound interest is : ${a-pamt:.2f}");