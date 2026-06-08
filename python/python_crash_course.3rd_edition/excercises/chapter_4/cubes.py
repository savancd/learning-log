# cubes

# A number raised to the third of power is called a cube. 
# For example, the cube of 2 is written as 2**3 in Python.
# Make a list of the first 10 cubes that is the cube is each integer
# from 1 to 10 and use a loop to print the value of each cube

import math

# creating a list of 30 numbers
numbers = [value for value in range(1, 31)]
# joining a list to be 10 numbers and printed as 12345678910
first_10  = numbers[:10]
#joined = "".join(map(str, first_10))


print(f"The new list is: {first_10}\n\n")


for n, num in enumerate(first_10):
	n =+ 1
	result = int(num)**2
	print(f"The number {n} is: {num} || {num} ** 2 =  {result}")


