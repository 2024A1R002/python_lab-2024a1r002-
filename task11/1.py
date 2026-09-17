#write a python program to input marks of n student in a list .display highest marks, lowest marks, average marks and number of student who passed
n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    x = int(input("Enter marks: "))
    marks.append(x)

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Average marks:", sum(marks) / n)

count = 0

for x in marks:
    if x >= 40:
        count = count + 1

print("Number of students passed:", count)