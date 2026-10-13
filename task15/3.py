#write a program to perform serching activity using linerar and binary search
n  = list(map(int,input("enter ").split()))
target = int(input("enter number to find"))

for i in range(len(n)):
    if n[i]== target:
        print("position",i+1)
        break
else:
    print("not found")



n.sort()    

low = 0
high = len(n)-1
while low <= high:
    mid = (low+high)//2
    if n[mid]== target:
        print(mid+1)
        break

    elif n[mid]<target:
        low = mid+1
    else:
        high = mid -1
else:
    print("element not found")                





