#write a python program to take a string and separate charactes present at even index positions and odd index position
s = input("enter string:")
c = input("enter separate char")
even_chars = s[::2]
odd_chars = s[1::2]
print("Characters at even indices:", even_chars)
print("Characters at odd indices:", odd_chars)