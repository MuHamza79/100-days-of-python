#Factorials
#fact(5) = 5*4*3*2*1 = 120
#fact(3) = 3*2*1 = 6
#fact(0) = 1

#HENCE fact(n) = n*fact(n-1)

#defining recurisive funtion 
def fact(n):
    if n == 0 or n == 1 :
     return 1
    else:
        return n*fact(n-1)
    
# taking input from user
print("This program will calculate the factorial of a number")
num = int(input("Enter a number:"))

#diplaying resluts
print(f"Number is {num} and its factorial is {fact(num)}")


# TRACING WITH fact(5)
# 5*fact(4)
# 5*4*fact(3)
# 5*4*3*fact(2)
# 5*4*3*2*fact(1)
# 5*4*3*2*1



# Fibonacci Series
#fn = f(n-1) + f(n-2)

#defining recursive function
def Fibonacci(x):
    if x == 0:
        return 0
    else:
        if x ==1 :
            return 1
        else:
            return(Fibonacci(x-1) + Fibonacci(x-2))
#taking user input
number = int(input("Enter a number till you want to display the Fibonacci series:"))
#   Displaying resultsss
for i in range(number):
    print(Fibonacci(i))

        
    
