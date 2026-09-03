#write a python program to take an email address and print the domain name
email = input("Enter email address: ")
index = email.find("@")
domain = email[index+1:]
print(f"Domain name: {domain}")   
