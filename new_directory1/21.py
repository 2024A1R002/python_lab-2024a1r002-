#writea python program to fill the given letter templte with name and date
# name = input("Enter name: ")
# date = input("Enter date: ")
# print(f"Dear {name}, You are selected! Date: {date}")

name = input("Enter name: ")
date = input("Enter date: ")
letter = "Dear [name], You are selected! Date: [date]"
letter = letter.replace("[name]", name)
letter = letter.replace("[date]", date)
print(letter)