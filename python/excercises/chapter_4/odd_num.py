# Odd Numbers

# use third argument of the range() function to make a list of the odd numbers from 1 to 20
# Use for loop to print the numbers in a list


# importing random  library
import random

# generating numbers
numbers = [value for value in range(1, 21, 2)]

# Enumerating and printing the message on the screen
for n, num in enumerate(numbers):
	n += 1
	print(f"The number {n}: {num}")


