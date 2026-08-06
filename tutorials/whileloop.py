#WHile loop
i = int(input("Enter a number: "))
while i<=10:
    i = int(input("Enter a number: "))
    print("you entered",i)
    
print("Loop complete")

# Decrement loop
i = 3
while i>0:
    print(i)
    i = i-1
    
# WHILE + ELSE loop
num = -5
while num>0:
    print(num)
    num = num-1
else:
    print("The loop is over")