#write a python program to  print a centerd pyramid using stars
n = int(input("enter number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()                        