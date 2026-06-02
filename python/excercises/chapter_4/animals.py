# Animals 
# three different animals make in the list
# that have similar characteristics
# use a for loop to print each animal name
# modify program to print custom message together with a name of animal


# making a list, Empty list
animals = []


# taking user input for three animals inputs
print("Please Enter three animals that you think are in some way similar:\n")

times = 3

# Taking 3 inputs from a user
for i in range(3):
	# taking i and making to start at 1 and not at 0
	i += 1
	# append user input into a list
	user = input(f"{i}: ") # taking i as a numbering for each user input
	user = user.title()
	animals.append(user)

print(30 * "=")



for i, name in enumerate(animals):
	i += 1
	print(f"{i}: {name} can be a great pet!")


print("All this Animals have in common that they are great companions to people and great pets.")
