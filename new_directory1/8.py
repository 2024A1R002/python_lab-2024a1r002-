#write a a python program to calculate simple interset and total amount using principal,rate and time enetered by the user
principal = float(input("enter the principal amount: "))
rate = float(input("enter the rate of interest: "))
time = float(input("enter the time in years: "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
print(simple_interest)
print(total_amount)