# name ="Muhammad Hamza Arshad Satti"
# for character in name: 
#     print(character)
#     if character == "z":
#         print("It is a unique name.")
#     else: 
#         print("It is not a unique name.")
        
name2 = input("Enter your name: ")
x = 0
for character in name2:
    if character == "z" :
        x = 1
if x == 0:
    print("It is not a unique name.")
else:
    print("It is a unique name.")
    
    
colors = ["red" ,"green" ,"yellow","purple","blue","orange"]
for color in colors:
    print(color)
        
        
#printing num till 1-20 except 0 and 10
for num in range(21):
    if num == 0:
        continue
    if num ==10:
        continue
    print(num)
    
# dynamincs of range function
for num in range(1,11):
    print(num+1)
for num in range(5):
    print(num-2)
       
#print odd num b/w 1-10
for num in range(1,11,2):
    print(num, "It is an odd number.")
    
#print even num b/w 0-10
for num in range(0,11,2):
    print(num ,"It is an even number.")
      
        
        
    