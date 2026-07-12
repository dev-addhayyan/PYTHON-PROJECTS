x=input("Enter email to get username  : ")
#asking user to enter email so that we can get username from it
y=x.split("@")
#splitting the email from @ to get username
print(y[0])