#take a sentence combining double spaces and unwanted spaces at the beginning or end clean the sentence
sentence = input("enter sentence:")
sentence = sentence.strip()
sentence = sentence.replace("  ", " ")
print(sentence)