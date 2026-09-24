#write a python program to input two lists and create a third list containing common elements
a = list(map(int, input("Enter first list: ").split()))
b = list(map(int, input("Enter second list: ").split()))

c = []

for i in a:
    if i in b:
        c.append(i)

print("Common elements:", c)
