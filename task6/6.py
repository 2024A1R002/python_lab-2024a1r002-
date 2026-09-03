#write a python program to take a word and count the number of vowels a,e,i,o,u
word = input("enter word:")
vowel_count =0
for char in word:
    if char.lower() in 'aeiou':
        vowel_count += 1
print(vowel_count)        