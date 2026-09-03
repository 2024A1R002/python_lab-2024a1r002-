#take an email address and check whether it contain @ and .com
email_address = input("enter email address:")
if '@'in email_address and '.com' in email_address:
    print("Valid email address")
else:
    print("Invalid email address")