# One million

# create a list of numbers from 0 to 1million

# creating empty list
num_list = []

# making a numbers to go up to 1million
for i in range(1, 1_000_001):
	# appending the numbers to the empty list
	num_list.append(i)
	# printing each number separatelly
	#print(len(num_list))

minimal = min(num_list)
#max_result = ", ".join(map(str, num_list))
maximum = max(num_list)
#max_result.replace("_", ".")


#maximum = max(num_list).replace("_", ".")

print(f"This is smalest number in the list: {minimal}")
print(f"This is largest number in the list: {maximum}")


# number = [value for value in range(1, 1000001)]

# print(num_list)
