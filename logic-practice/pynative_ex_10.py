#Exercise 10. Finding Extremes (Min/Max) in a List

#initializing a list
numbers = [45 , 2 , 89 , 12 , 7]

#sorting the list
numbers.sort()

#displaying results
print("The smallest number in the list is", numbers[0])
print("The largest number in the list is", numbers[4])


# METHOD 2

#initializing a list
numbers = [45 , 2 , 89 , 12 , 7]
#using max/min functions
largest = max(numbers)
smallest = min(numbers)
#displaying results
print(f"Largest number is {largest} and smallest number is {smallest}")