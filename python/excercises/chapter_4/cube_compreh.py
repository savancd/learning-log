# cube comrehension

# Use a list comprehension to generate a list of the first 10 cubes


# gemerating a list  of cubes
cubes = [value for value in range(1, 11)]

for n, num in enumerate(cubes):
	n += 1
	result = num ** 2
	print(f"The number {n} is: {result}")

