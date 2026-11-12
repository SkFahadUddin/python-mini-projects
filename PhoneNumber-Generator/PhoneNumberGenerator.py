#Phone number generator

import random

print(f" Phone Generator !! ")
def greet(firstname,lastname,greetings):
    print(f"{greetings}{firstname} {lastname}.")

def numgenerator():
    for i in range(10):
        print(f"{random.randint(0,9)}", end="")

name1=input("Enter your First name : ");
name2=input("Enter your Last name : ");
ccode=int(input("Enter your Country Code : "));

greet(firstname=name1,lastname=name2,greetings="Hello , ")
print(f"+{ccode} " ,end="")
numgenerator()