#write a python program to rotate  a list one postion to the right
a = list(map(int, input("Enter numbers: ").split()))

last = a.pop()
a.insert(0, last)
print("Rotated list:", a)

