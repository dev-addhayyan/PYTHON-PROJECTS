x=input("Set Password : ")
#asking user to set password
if len(x) >= 8 and "@" in x and "." in x:
    print("Password is valid")
else:
    print("Password is not valid. Password should be at least 8 characters long and contain '@' and '.'")