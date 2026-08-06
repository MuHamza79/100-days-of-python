age = int(input("Enter your age :"))
print("Your age is",age)
# CONDITIONAL OPT
 # > , < , >= , <= , == , !>
print(age > 18)
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
num = int(input("Enter a number :"))
if num > 0: 
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
    
    
# Nested IFS
number = int(input("Enter a number :"))
if number < 0:
    print("The number is negative")
elif number > 0:
    if number <= 10:
        print("The number is b/w 1 to 10. ")
    elif number >= 10 and number <= 20:
        print("The number is b/w 10 and 20.")
    else: 
        print("The number is greater than 20.")
else:
    print("The number is zero")
      
    