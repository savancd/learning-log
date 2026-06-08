# threes

# Make a list of mulitples 3, from 3 to 30. Use for loop to print the numbers in your list


# creating the list of numbers
numbers = [value for value in range(1, 31)]
# creating empty list 
multiples_of_3 = []

# for loop
for num in numbers:
	# if the number is divisible by 3 and it's equal with 0
	if num % 3 == 0:
		# it's gonna append it to the new created list
		multiples_of_3.append(num)


# printing it to the screen and enumerating with a message
for n, num in enumerate(multiples_of_3):
	# starting from 1 and not from 0
	n += 1
	# calculating every number
	result = num / 3
	# printing to the screen
	print(f"The number {n} is: {num} || {num} / 3 =  {int(result)}")
