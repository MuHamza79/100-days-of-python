#Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

#Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

#taking integers as input
num1 =int(input("Enter the first number:"))
num2 =int(input("Enter the second number:"))
#calculating product
prod = num1*num2
sum = num1+num2
#determining output
if prod <=1000:
    print("The product of" , num1 , "and" ,num2 ,"is" ,prod)
else:
    print("The sum of", num1, "and", num2, "is", sum)