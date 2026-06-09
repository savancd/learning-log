#===========================================================================#
# File: fake_id_card.py
# Author: Sava Maksimović
# Created: 8 June 2026
# Description: Mini‑project:ID card. Build a “fake ID card” displaying user
# ### personal info
# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#

# Importing library for the project
import datetime
import random
import uuid
import json
import inquirer

inputs = []

# loading .json file to read it from a file
with open("places.json", "r") as file:
	data = json.load(file)

# Printing welcome message and asking for data input
print("Welcome to your ID CARD\nPlease enter your data:\n")
print("ID CARD")

# While it's true it's gonna run until break
while True:
	# asking from user full name
	user_name = input("Name: ")

	# append to list name
	inputs.append(f"Name: {user_name}")

	# If the user enter anything that is not a letter or a space, its gonna run
	if user_name and all(ch.isalpha() or ch.isspace() for ch in user_name):
		# Printing if its good
		# print(f"Name: {user_name}")
		# breaking the loop if its good
		break
	else:
		# if the user enters some numbers its gonna print it and try agein
		print(f"Enter only letters and spaces!")

print(30 * "=")

# Printing for user message to input DOB(date of birth) in correct format
print("Enter your date of birth (DD.MM.YYYY)")
# asking for input for DOB
while True:
	# input from a user
	dob = input("DOB: ")

	# append to list date of birth
	inputs.append(f"DOB: {dob}")

	# taking date input  and breaking the loop if it's correct one
	try:
		date_of_birth = datetime.datetime.strptime(dob, "%d.%m.%Y")
		inputs.append(date_of_birth)
		break
	# printing error onto screen if the format is not correct
	except ValueError:
		print("Incorect format. Please input it as is: DD.MM.YYYY")

print(30 * "=")

# Generating unique ID with uuid
def short_uuid(i=8):
	return uuid.uuid4().hex[:i]

identifier = short_uuid(8).upper()

# append to the list
inputs.append(f"ID Number: {identifier}")

# print(f"ID No: {identifier}")

print(30 * "=")

# Asking user to choose current address
print("Please choose  your current address!\n")

# pulling out places (cities) from a .json file
places = data.get("Places") or data.get("places") or []

# enumerating the list
for n, place in enumerate(places):
	n += 1
	# printing number of the choice and the name of the city
	print(f"{n}: {place.get('city')}")

# Asking the user to enter the number from a list above
question = [
	inquirer.Text(
		"choice_num",
		message="Enter the number of your choice",
		validate=lambda _, x: x.isdigit() and 1 <= int(x) <= len(places)
	)
]

# validate checks the user input and returns True
# 1 <= int(x) <= len(places) check is it integer in the choice option range


# prompts the inquirer
answers = inquirer.prompt(question)
# retrives the user input
choice_index = int(answers["choice_num"]) - 1
selected_place = places[choice_index]



# this is type test
#print(selected_place)
#print(type(selected_place))

select_list = list(selected_place.items())

# this is type test
#print(type(select_list))

for n,(key, value) in enumerate(select_list):
	n += 1
	print(f"{n}: {value}")

	# Append address
	inputs.append(f"Address:  {value}")


# test
#print(select_list, type(select_list))

issuing_list = []

# convering it to dict to print it
select_list_dict = dict(select_list)
# printing ID issuing country
print(f"Issuing country: {select_list_dict['country']}\nIssue Date: {datetime.datetime.now().strftime('%d.%m.%Y')}")

inputs.append(select_list_dict["country"])
today = datetime.datetime.now().strftime("%d.%m.%Y")
inputs.append(f"Issuing country: {today}")




print(30 * "=")
print(30 * "=")

#print(f"{name_list}\n{id_number_list}\n{address_list}\n{issuing_list}")
print(inputs)


#for n, (key, value) in enumerate(inputs):
#	n +=1
#	print(f"{n} {key} {value}")











