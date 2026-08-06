# Multiplication table 
print("Enter multiplaction table 1-12:")
table = int(input())
while table < 0 and table > 12:
    print("Enter a number b/w 1 to 12")
    table = int(input())
count = 1
for count in range(1,12):
    print(table ,"x" ,count , "=" , table*count)
    if count == 10:
        break
print("The loop is over")




for i in range(1,10,1):
    if i == 5:
        print("This number is skipped")
        continue
    if i == 9:
        print("Loop over")
        break
    print(i)
    
    
#printing only even numbers from a list
list = [0,1,2,3,4,5,6,7,8,9,10]
for i in list:
    if i % 2 != 0 :
        continue
    print(i)
        
        
#DO WHILE LOOP
i = 0
while True:
    print(i)
    i=i+1
    if i % 100 == 0:
        break
    
        
