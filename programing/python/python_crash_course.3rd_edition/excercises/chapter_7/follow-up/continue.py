import time

# printing odd numbers
current_num = 6

# looping through numbers
while current_num > 5:
	# increasing the number with each loop
	current_num += 1
	# waiting time between numbers
	time.sleep(.5)
	# while number is dividable by 2
	if current_num % 2 == 0:
		continue

	print(current_num)

