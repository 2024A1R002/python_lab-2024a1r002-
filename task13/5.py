# write a python program to check whether  a given value is present in tuple if present display the position
t = tuple(map(int,input("enter value").split()))
n = int(input("enter the value to serch"))
if n in t:
    print(t.index(n))
else:
    print("value is not presnt")    
