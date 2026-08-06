a="1"
b="2"
print(a+b)# this will give 12
print(int(a)+int(b)) #this will give 3
#Explicit TYPE CONVERSION
c=7
d="The number is"
#print(d+c)this gives error
print(d + str(c)) # this adds both strings

#Implicit TYPE CONVERSION
a=2
b=3.0
print(a+b) #converted to float
