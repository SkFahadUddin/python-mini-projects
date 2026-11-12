#Program to write a username with not containing spaces,digit and not more than 12 characters
print(f"Enter a username with not containing spaces,digit and not more than 12 characters : ");
username=input();
if(username.isalpha() and len(username)<=12):
    print(f"Your username is : {username}");
else:
    print(f"Invalid username");