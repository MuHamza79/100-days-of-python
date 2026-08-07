#Exercise 13. Filtering Lists with Conditional Logic


num_list = [10, 20, 33, 46, 55]
print("Given list is", num_list)
print("Divisible by 5:")

# Iterate through each element
for num in num_list:
    # Check divisibility
    if num % 5 == 0:
        print(num)