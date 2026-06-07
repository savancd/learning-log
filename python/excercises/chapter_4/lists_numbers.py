# Statisticts with a list of numbers 

import random


# creating a list of numbers
numbers_list = []

# generating random numbers for a list
for i in range(30):
	# appending to the list random numbers
	numbers_list.append(random.randint(1, 1001))

# Printing all the numbers
print("These are numbers from a list: ", numbers_list, "\n\n")


# To find maximum 
print("This is the maximum: ", max(numbers_list))

# To find minimum
print("This is the minimum: ", min(numbers_list))

# To calculate all the digits
print("This is calculation: ", sum(numbers_list))


