#take student full name and rollnumber generate email using first 3 letter of first name, first 3 letter of last name, and last 3 chracter of roll number
#

full_name = input("enter full name")
roll_number = input("enter roll number")
space_index = full_name.find("")

first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

email = first_name[:3] + last_name[:3] + roll_number[-3:] + "@gmail.com"
print("Generated email:", email)