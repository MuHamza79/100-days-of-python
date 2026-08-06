# initialize tupples
tup = (1,3,4,5,6,7,8,3,"green",True)
print(tup)


# tup[3]=10
# print(tup) # this would throw an error


print(tup[4])
if 5 in tup:
    print("5 is present")
else:
    print("5 is not present")
    
animals = ("cat","dog","rat","bee","ant","cow",)
print(animals[3:6])
print(animals[-6:-2])


#Tuples to List
countries = ("pakistan","india","bangladesh","sri lanka","afghanistan")
newlist = list(countries)
newlist.append("Japan")
newlist[1]= "America"
countries = tuple(newlist)
print(countries)


# TUPLE METHODS
#1. count ()
tuple1 = (1,2,2,3,4,2,3,4,2,1,2)
counter = tuple1.count(2)
print("The number of 2's in the tuple is" , counter)

#2. index()
tuple1 = (1,2,2,3,4,2,3,4,2,1,2)
index = tuple1.index(2)
print("The index of 2 is" , index)

index1 = tuple1.index(3,4,9)
print("The index of 3 is" , index1)