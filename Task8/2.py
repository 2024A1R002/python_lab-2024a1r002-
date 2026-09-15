# write a python program to simulate a digital lock system.
#the lock should ask the user to enter a 4 digit PIN. if the enterd pin does not contain exactly 4 digits the prpogram shoould display an error message and sak again. if the enterd pin is correct, the lock should open. Otherwise the program should ask the user to try again.

correct_pin = "2500"

while True:
    user_pin = input("Please enter the 4-digit PIN: ")
    
    if len(user_pin) != 4:
        print("Error: Please enter exactly 4 digits.")
        continue
    
    if user_pin == correct_pin:
        print("Lock opened successfully!")
        break
    else:
        print("wrong  PIN. Please try again.")