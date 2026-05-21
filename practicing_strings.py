# Reversing a string 
name = "Python"
print(name[::-1])

#length of string
name=input("Enter name: ")
print(len(name))

#upper case
name = "python"
print(name.upper())

#lower case 
word = input("Enter word: ")
print(word.lower())

#Replacing a word 
sentence = "I love java"
print(sentence.replace("java","Python"))

#split string
email = "sai@gmail.com"
print(email.split("."))

#Removing extra spaces
name="     python    "
print(name.strip())

#palindrome checker
word = input("Enter word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
    

