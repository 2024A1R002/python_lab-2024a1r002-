#write a python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit
n = int(input("Enter a number: "))
while n>=10:
    sum =0
    while n>0:
        digit = n%10
        sum = sum + digit
        n = n//10
    n = sum
print("The single digit sum is:",n)        
