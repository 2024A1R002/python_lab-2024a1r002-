#write a python program to take  total minutes as input and convert into hour and remaining minutes
total_minutes = int(input("Enter total minutes: "))
hours = total_minutes // 60
remaining_minutes = total_minutes % 60
# print(f"{total_minutes} minutes is equal to {hours} hours and {remaining_minutes} minutes.")
print(hours)
print(remaining_minutes)