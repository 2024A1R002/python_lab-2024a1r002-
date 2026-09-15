# write a python program to print numbers from 1 to 50 but skip all numbers divsible by 4
n = int(input("Enter a number: "))
for i in range(1,51):
    if i%4!=0:
        print(i)
