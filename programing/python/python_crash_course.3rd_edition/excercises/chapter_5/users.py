#===========================================================================#
# File: users.py
# Author: Sava Maksimović
# Created: 18 June 2026
# Description: Mini‑challenge for Python Crash Course book
# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#



# make a list with usernames, including the admin
# print a greeting to each person

# importing library
import json

# loading the .json file
with open("./files/users.json", "r") as file:
	data = json.load(file)

with open("./files/new_users.json", "r") as file_2:
	data2 = json.load(file_2)

# printing the json file with 4 spaced indentation
#print(json.dumps(data, indent=4))

# anumerating list of users
for n, name in enumerate(data):
	# starting from 1 and not 0
	n += 1

	# printing it to the screen
	# name.get("name") to get a name of a person from a dict
	# if there is no name.get it would compare a dict with a string "Eve Admin"
	# it would be always False in that way, that is the reason why it must have
	# name.get("name") and then compare it to string "Eve Admin"
	if name.get("name") == "Eve Admin":
		print(f"{n}: Hello  {name['name']}, would you like to see status report?.")
	else:
		# printing message to each person
		# if the person is male its gonna print actor
		# if it's the woman then message will be "actress"
		if name.get("gender") == "f":
			print(f"{n}: Hello {name['name']}, Thank you for being amazing actress. ")
		else:
			print(f"{n}: Hello {name["name"]}, Thank you for being amazing actor.")

	# creating variable name "movies" and get from a name of the person 
	# targeting the "known_movies"
	movies = name.get("known_movies")
	# isinstance checks is the object and instance of a given class and returns
	# True or False
	if isinstance(movies, list):
		# iterating through the list of objects from a movie in movies
		for movie in movies:
			# printing it to the screen and placing "(-)" on the start
			if movie: # checking is it string empty or not
				print("    -", movie)
	print("")



print(30 * "=")
print("Cheking new users...")
print(30 * "=")

print("Please Enter user name you want to use:")
user_name = input()

exists = False

# checking is the user exists
for name in data2:
	if isinstance(name, list):
		if name.get("name") == user_name:
			exists = True
			break

if exists:
	print(f'{name["name"]} name is existing already.')
else:
	print(f"{user_name} name is available")

	data2.append({"name": user_name})

	print(f"Saving {user_name} to user list...")
	with open("./files/new_users.json", "w") as f:
		json.dump(data2, f, indent=4, ensure_ascii=False)


#print(user_name)
for name in data2:
	print(name.get["name"])




