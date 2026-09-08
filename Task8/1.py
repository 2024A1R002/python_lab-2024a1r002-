#write a python program to determine whether a student is eligible for a scholarship
# trhe student has a cgpa of 8.5 or above  and attendance of 85 percent or above.
#the student has won a national level cometition
#The program shoul take cgpa, attendance percentage and national level competition status as input then display whether the student is eligible for the scholarship
cgpa = float(input("enter cgpa"))
attendance = int(input("enter attendance"))
national_level_competition = input("enter national level competition status (yes/no): ")

if cgpa>=8.5 and attendance>=85 and national_level_competition=="yes":
    print("eligible for scholarship")
else:
    print("not eligible")    
