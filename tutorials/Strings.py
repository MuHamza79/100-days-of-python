name = 'hamza'
print("Hey" , name)

#To include Double quotations as part of string
#Method 1.
print("Hamza said,\"I am fine!\"")

#Method 2
print('Hamza said, "He needs an apple"')

#Indexing --> starts from [0]
fruit = 'apple'
print(fruit[0])
print(fruit[3])
print(fruit[4])

print("Lets use a for loop\n")
count = 0
for characters in fruit:
    print(characters)
    count = count +1
    
print("There are" , count , "characters in" , fruit)



# STRINGS SLICING AND COUTNING
fruit = input("Enter a fruit: ")
length = len(fruit) #this will give the length of the string
print("The length of" , fruit , "is" , length)

print(fruit[0:5])
names="HAMZA ARSHAD"
print(names[0:5])
print(fruit[0:-3]) # this will print everything except the last 3 characters as mango is 5 characters long
                   # so 5-3 = 2 hence it would be considered as 0 to 2 characters
print(fruit[-1 : -4])
print(fruit[-3 : -1]) #this will print 5-3=2 and 5-1= 4 so it will print 2 to 4

nm = "harry"
print(nm[-4 : -2])

# UPPER and lower Function
##STRINGS ARE IMMUTABLE
str1 = "abcdef"
print(str1.upper())
str2 = "ABCDEF"
print(str2.lower())

# STRIP FUNCTION
greeting = "Hello!!!!"
print(greeting.rstrip("!"))

greet = "!!!!!!!Hello!!!!!!!"#### Removes only trailing characters
print(greet.rstrip("!"))#### "!" AT START WILL REMAINNNNNN

#REPLACE FUNCTION
str3 = "!!!Hamza!!!!ARSHAD!!!ARSHAD"
print(str3.replace("Hamza" , "Arshad")) # 1st parameter wanting to be changed

str3 = "!!!Hamza!!!!ARSHAD!!!ARSHAD"
print(str3.replace("ARSHAD" , "Hamza")) # 2nd paramenter that will replace the 1st

#SPLIT FUNCTION
str4 = "Muhammad Hamza Arshad Sattti Khan"
print(str4.split(" "))  #this will split the string into a list at each empty space [ " " ]

# CAPITALIZE function
Heading = "introduction to python" # capitalizes the first character
print(Heading.capitalize()) 

head = "Earth the planet" #If already capital ; capitalize function has no effect.
print(head.capitalize())

blogheading = "Earth - A HOme" # capitalize only first character and remaining characters are turned to lowercase
print(blogheading.capitalize())

# CENTER FUNCTION
name1 = "My name is Hamza"
print(len(name1))
print(name1.center(50))
print(len(name1.center(50)))

# Count function
spell = "Abracadabra"
print(spell.count("A"))

# ENDSWITH FUNCTION
word = "Hello!!!" 
print(word.endswith("!")) # returns True
print(word.endswith("?")) # returns False
str5 = "Welcome to the console!"
print(str5.endswith("to", 5 , 9 ))


# Find function
sentence = "his name is Hamza.Hamza is a good boy"
print(sentence.find("is"))
print(sentence.find("by")) # this will give -1 as there is no "by" in the sentence
# index function
print(sentence.index("is"))
#print(sentence.index("Haris")) # this would give error as index forces to find he element in string

# ISALNUM FUNCTION
str6 = "abc123"
print(str6.isalnum()) # CHEKS IF STRING IS ALPHANUMERIC

#ISALPHA FUNCTION
str7 = "abccdEEEWE"
print(str7.isalpha())

#ISLOWER FUNCTION
str8 = "helloW"
print(str8.islower())

#ISNUMERIC FUNCTION
str9 = "123"
print(str9.isnumeric())

#ISPRINTABLE FUNCTION
str10 = "abc . \n cde"
print(str10.isprintable())

#ISUPPER FUNCTION
str11 = "HELLO"
print(str11.isupper())

#Isspace FUNCTION
str12 = " "
print(str12.isspace())

#istitle FUNCTION
str13 = "Hello World"
print(str13.istitle())

#startswith FUNCTION
str14 = "Hello World"
print(str14.startswith("Hello"))

#TITLE FUNCTION
str15 = "hello world"
print(str15.title())