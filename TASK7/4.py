#take name branch year generate a code name using string concatenatioon slicing and repetition 
name = input("enter name")
branch = input("enter branch")
year = input("enter year")
code_name = name[:3] + branch[:3] + year[-2:]
print("*" * 30)
print("student Code:",code_name)
print("*"* 30)
