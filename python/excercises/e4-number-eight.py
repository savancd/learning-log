
# Try it yourself chalenge
# write addition, substraction, multiplication, and division
# operations that each result in the result number 8. Be sure to enclose your operation
# in print() calls to see the results. You should create four lines that look like this:
#
# print(5 + 3)
#
# Your output should be four lines, with the number 8 appearing one on each line.


# adding variables with calculations
addition =  4 + 4
subtraction =  12 - 4
multiplication = 4 * 2
division =  16 / 2

# making empty list
lista = []

# placing all calculations into a list
lista.append(addition)
lista.append(subtraction)
lista.append(multiplication)
lista.append(division)


# anumerating to make every calculated number in their own respective number
for i, num in enumerate(lista):
	#  Calculating the "i" to start at 1 and not at 0
	i += 1
	# printing it to the screen
	print(f"Number {i}: {num}")

