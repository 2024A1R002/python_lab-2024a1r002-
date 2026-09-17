#write a python program to input a list of numbers  and create a new list  containing only unique element
a = list(map(int, input("Enter numbers: ").split()))

unique = []

for i in a:
    if i not in unique:
        unique.append(i)

print("Unique elements:", unique)


