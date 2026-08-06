# previous_num = 0
# for num in range(10) :
#     print("Current number is" ,num)
#     previous_num = num
#     print("Previous number is" , previous_num)
#     print("The sum is" ,num + previous_num)
    
# Exc 1 : PRINTING CURRENT NUM / PREVIOUS NUM / SUM
previous_num = 0
for num in range(10) : 
    sum = num + previous_num
    print(f"Current number is {num} and previous number is {previous_num} and sum is {sum}")
    
    previous_num = num
    
    
    
# Exc 3 :
text = "pynative"
print("The oringinal word is ",text)
print("Printing only even characters")
# format [start:end:step]

even_char = text[0::2]
for i in even_char:
    print(i)
    
word = input("Enter a word:")