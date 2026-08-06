# # COMMENTS , ESCAPE SEQUENCE & PRINT STATEMENTS
# print("Hello! How are you?\nWhat is you name?")
# print("Hello World") #this is printing Hello world
#  #for multi-line comments
# p=7
# if p>5:
#     print("p is greater than 5")
# else:
#    print("p is less than 5")
# '''
#     This is a multi-line comment
#     written in
#     more than just one line
# '''
# #ESCAPE SEQUENCE for quotation marks in strings
# print("My name is \"Hamza\"")
# print("What are you doing?\"playing?\"")
# print("Sara said to Ali,\"I am fine!\"\nAli said to Sara,\"I am also fine.\"")
# # PRINT STATEMENTS( parameters)
#  #1. Separators
# print("hey", 6 , 7)
# print("hey", 6 , 7 , sep="~")
# print("hey", 6 , 7 , sep=":")
#  #2. End
# print("hey", 6 , 7 , sep="~" , end="*\n")
# print("hey", 6 , 7 , end="*\n")
# print("hey", 6 , 7 , end="**")


#Variables and data types
a=1
print(a)
b="Harry"
print(b)
#adding string in string
c="Harry is a good boy"
d="hamza is excellent"
print(c+d)
print ("The type of a is" , type(a))
print ("The type of b is ", type(b))
print ("The type of c is" , type(c))
print ("The type of d is" , type(d))

#List and tuples
##Lists are Mutable i.e they can be changed
list=[1,2,3,4,5 ,6.7 ,["apple" , "banana" , "cherry"]]
print(list)
##Tuples are Immutable i.e they can not be changed
tuple=[1,2,3,4,5 ,6.7 ,["apple" , "banana" , "cherry"]]
print(tuple)

#Dictionary
dict={"name":"hamza", "age":17 , "gender":"male"}
print(dict)
print(dict["name"])
