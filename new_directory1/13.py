#write a python program to take 2-digit number as input and print the sum of its digit
number = int(input("enter 2-digit number"))
sum = (number //10)+(number%10)
print(sum)