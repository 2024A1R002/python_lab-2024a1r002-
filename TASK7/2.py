#take roll number like 2024A1R002 and extact admission year program code and roll number digit using slicing
roll_number = input("enter roll number")
admission_year = roll_number[:4]
program_code = roll_number[4:6]
roll_number_digit = roll_number[-3:]
print("Admission Year:", admission_year)
print("Program Code:", program_code)
print("Roll Number Digit:", roll_number_digit)