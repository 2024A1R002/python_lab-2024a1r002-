#write a pytghon program to input a decimal number and convert it  into binary without using built in function
n = int(input("enter number"))
binary = ""
while n>0:
    binary = str(n%2)+binary
    n = n//2
print("Binary number is:",binary)
