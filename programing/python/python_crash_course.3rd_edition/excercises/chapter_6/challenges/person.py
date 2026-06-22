# use a dictionary to store information about a person 
# store their girst name, last name, age, city.
# print each information 




information = {"name": "jon", "last_name": "done", "age": 66, "city": "singapore"}


# checking what are the existing keys in the dict and printing them
for i, n in enumerate(information.values()):
	i += 1
	# checking if the value is the "int"
	# if it is it's printing it to the screen
	if isinstance(n, int):
		print(f"This is value {i}: {n}")
	# if the value is the str and not int 
	# it's gonna capitalize it "title()"
	else:
		n = n.title()
		print(f"This is value {i}: {n}")


print(30 * "=")

# same as previous just printing the keys and not values
for i ,n in enumerate(information):
	i += 1
	if isinstance(n, int):
		print(f"This is a key {i}: {n}")
	else:
		n = n.title()
		print(f"This is key {i}: {n}")

print(30 * "=")

# printing the value from a key 
print(f"This is name: {information['name'].title()}")
print(f"This is last name: {information['last_name'].title()}")
print(f"Age: {information['age']}")
print(f"City: {information['city'].title()}")
