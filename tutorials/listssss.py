list1 = [1,2,3,4,5,6,78]
list2 = ["red","green","blue","yellow"]
print(list1)
print(list2)
print(list1[4])
print(list2[2])

#negative index
# [len(list2)-1] i.e 4-1=3 will print yellow
print(list2[-1])
print(list2[-2])
print(list2[-4])


#Presence checks
if 2 in list1 :
    print("2 is present")
else:
    print("2 is not present")
    
if "orange" in list2 :
    print("present")
else:
    print("not present")
    
    
#RANGE OF INDEX
animals = ["cat","dog","lion","tiger","elephant","monkey",]
print(animals[2:5])
print(animals[-6:-3])


#list comprehension
lst = [x*x for x in range(11)]
print(lst)

# names = ["Hamza","Arshad","Satti","Khan"]
# listWith_i = [i for i in names if "i" in names]
# print(listWith_i)

list404 = [x*x for x in range(10) if x%2==0]
print(list404)


# List methods
#1.append
num = [1,3,5,7]
num.append(9)
print(num)
#2. List sorting A.O/D.O
numbers = [6,7,4,32,1,2,5,7,8,9,6,4,32,1]
numbers.sort()
print(numbers) # this will sort in A.O

numbers.sort(reverse=True)
print(numbers) # this will sort in D.O

#3. Reverse ()
digits = [10,9,8,7]
digits.reverse()
print(digits) # reverses the order of orginial list

#4. Index()
color = ["red","green","blue","yellow"]
print(color.index("blue")) #gives position of the 1st occurance of the list item

#5. Count()
num = [1,1,1,4,2,1,2,4,4,5,31,1,2,3,1]
print(num.count(1))

#6. Copy()
color = ["red","green","blue","yellow"]
newlist = color.copy()
print(newlist) # this will copy the elements of the list to new list


#7. insert ()
color = ["red","green","blue","yellow"]
color.insert(1,"orange")
print(color)

#8. extend ()
even = [0,2,4,6,8,10]
odd = [1,3,5,7,9]
even.extend(odd)
print(even)

 # NOTEEE concatenating 
even = [0,2,4,6,8,10]
odd = [1,3,5,7,9]
num = even + odd
print(num)