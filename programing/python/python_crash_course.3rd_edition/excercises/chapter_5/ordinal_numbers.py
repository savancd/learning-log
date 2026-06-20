

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]



for n, i in enumerate(numbers):
	n += 1
	if i == 1:
		print(f"{n}: {i}st")
	elif i == 2:
		print(f"{n}: {i}nd")
	elif  i == 3:
		print(f"{n}: {i}rd")
	else:
		print(f"{n}: {i}th")
