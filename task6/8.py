#write a python program to take a sentence, detect double spaces, and replace them with single spaces
sentence = input("Enter sentence: ")
sentence = sentence.replace("  ", " ")
print(sentence)