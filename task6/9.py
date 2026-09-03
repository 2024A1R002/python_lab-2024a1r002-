#write a python program to take a word and print it in reverse order using slicing. Also check whether it is the same forward and backward
word = input("enter word:")
reversed = word[::-1]
if word ==reversed:
    print("The word is a palindrome")
    

