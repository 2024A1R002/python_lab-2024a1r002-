# 3write a python program to count how many times a particular element appersa in alist
a = list(map(int, input("Enter numbers: ").split()))

x = int(input("Enter element to count: "))

count = a.count(x)

print("Element appears", count, "times")
