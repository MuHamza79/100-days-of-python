#Exercise 9. Vowel Frequency Counter

#intializing variables
sentence = "Learning Python is fun"
vowels= "aeiou"
count = 0 

#determining the number of vowels
for char in sentence.lower():
    if char in vowels:
        count = count + 1

#displaying results
print("The number of vowels in the sentence is", count)