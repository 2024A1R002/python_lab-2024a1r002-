#write a python program to input numbers in alist and create two seperate list for even and odd numbers
a = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)