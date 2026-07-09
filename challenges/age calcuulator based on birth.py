x=int(input("CURRENT YEAR :"))
y=int(input("BIRTH YEAR :"))
z=int(input("CURRENT YEAR :")[-2:])

if x<1999:
    print("You are", 1900-1800-y+z, "years old.")
else:
    print("You are", x-y, "years old.")
