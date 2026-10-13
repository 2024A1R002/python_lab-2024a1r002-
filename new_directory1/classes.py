# 1.
# class Student:
#     def __init__(self,number):
#         self.number=number

#     def max_find(self):
#         max=number[0]
#         for i in range(1,len(self.number)):
#             if self.number[i]>max:
#                 max=self.number[i]
#         return max
# number=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     num=int(input("Enter number:"))
#     number.append(num)

# obj=Student(number)
# print("Maximum is:",obj.max_find())

# 2.
# class Count_even_odd():
#     def __init__(self,number):
#         self.number=number

#     def count_even_odd(self):
#         odd=0
#         even=0
#         for i in range(len(self.number)):
#             if self.number[i]%2==0:
#                 even+=1
#             else:
#                 odd+=1
#         return even,odd

# number=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     num=int(input("Enter number:"))
#     number.append(num)

# obj=Count_even_odd(number)
# print("Count of even odd numbers is:",obj.count_even_odd())

# 3.
# class Avg():
#     def __init__(self,number):
#         self.number=number

#     def avg(self):
#         sum=0
#         for i in range(len(self.number)):
#             sum+=self.number[i]

#         return sum/len(self.number)

# number=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     num=int(input("Enter number:"))
#     number.append(num)

# obj=Avg(number)
# print("Average of number is:",obj.avg())

# 4. 
# class Duplicate():
#     def __init__(self,number):
#         self.number=number
#     def dup(self):
#         dict={}
#         for i in range(len(self.number)):
#             if self.number[i] not in dict:
#                 dict[self.number[i]]=1


#         return list(dict.keys())

# number=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     num=int(input("Enter number:"))
#     number.append(num)

# obj=Duplicate(number)
# print("Average of number is:",obj.dup())

# 5. 
# class Student:
#     def __init__(self):
#         self.name=input("Enter name:")
#         self.roll=int(input("Enter roll number:"))
#         self.marks=int(input("ENter marks:"))

#     def display(self):
#         print(f"Name:{self.name}\nRoll:{self.roll} \n Marks:{self.marks}")

# obj=Student()
# obj.display()

s = input("enter a string")
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")    