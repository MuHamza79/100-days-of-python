'''def CalculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if a > b:
        print("1st is greater than 2nd")
    else:
        print("2nd is greater than 1st")

a = 9
b = 8
#if a > b:
#    print("1st is greater than 2nd")
#else:
#    print("2nd is greater than 1st")
isGreater(a,b)
# gmean1 = (a*b)/(a+b)
CalculateGmean(a,b)


c = 7
d = 6
#if c > d:
 #   print("1st is greater than 2nd")
#else:
 #   print("2nd is greater than 1st")
isGreater(c,d)
# gmean2 = (c*d)/(c+d)
CalculateGmean(c,d)'''




# FUNCTION ARGUMENTS

# 1--->>> DEFAULT arguments
def avg(a=9,b=1): # this becomes default
    print("The average is",(a+b)/2)
avg()
#avg(5,1) # this overrides the default

#example 2
def name(fname,mname="Arshad",lname="Satti"):
    print("Hello",fname,mname,lname)
name("Hamza")


#VARIABLE LENGTH ARGUMENTS
# Arbitary Arguments
def name(*name):
    print("Hello,",name[0],name[1],name[2])
name("Hamza","Arshad","Satti")


def name(*names):
    print("Hello:")
    for person in names:
        print("-", person)

# Now it works for 1, 3, or 100 names!
name("Hamza")
name("Hamza", "Arshad", "Satti", "Ahmed")



def avg(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print("The average is", sum/len(numbers))
    a = sum/len(numbers)
    return a
    
a = avg(1,2,3,4,5)
print(a)