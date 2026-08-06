#Exercise 6. Calculating Factorial with a Loop

num = 5
fact = 1

# range(start,stop,step)
# range excludes the stop value itself

for num in range (num , 0, -1):
    fact = fact*num

print("The factorial of 5 is", fact)