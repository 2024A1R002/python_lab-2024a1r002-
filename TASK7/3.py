#take an email address and print username domain and reversed domain
email_address = input("enter email address:")
username = email_address.split('@')[0]
domain = email_address.split('@')[1]
reversed_domain = domain[::-1]
print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reversed_domain)