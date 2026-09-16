#write a python program to print a square pattern of stars for n rows and n columns
n = int(input("enter number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*", end=" ")
    print()