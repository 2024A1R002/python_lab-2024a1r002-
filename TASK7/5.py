#take a password and check length presence of @ and whether first and last charcter are differnet
password = input("enter password")
print("length",len(password)>=8)
print("contain @",'@' in password)
print("first and last different",password[0]!=password[-1])

