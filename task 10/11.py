#write a python program to printan inverted right angled triangle using stars
n = int(input("enter number"))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()