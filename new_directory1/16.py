#write a python  program to swap two numbers without using a third variable
a  = int(input())
b = int(input())
a = a+b
b = a-b
a = a-b
print("after swapping:",a)
print("after swapping:",b)