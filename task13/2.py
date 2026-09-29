#write a python program to store all month names in a tuple input a month number and display the corresponding month name
month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

n = int(input("Enter month number: "))

print("Month is:", month[n-1])