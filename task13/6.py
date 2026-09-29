#wap in python to store one student data to a tuple,name,rollnumbers and marks display grade  based on marks


name = input("Enter student name: ")
rollno = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

student = (name, rollno, marks)

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Student Data:", student)
print("Grade:", grade)