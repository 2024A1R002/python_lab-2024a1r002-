#write a python program to take a student name and rollno then genrete a username usinfg the first 3 letter of the name and last 2 digit of the rollnumber
name = input("Enter student's name: ")
rollno = input("Enter student's roll number: ")
username = name[:3] + rollno[-2:]
print(f"username: {username}")