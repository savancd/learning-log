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
import re
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
	user_name = input("Name: ").title()

	# append to list name
	inputs.append(user_name)

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
	inputs.append(dob)

	if not re.fullmatch(r"\d{2}\.\d{2}\.\d{4}", dob):
		print("Format must be DD.MM.YYYY")
	else:
		try:
			date_of_birth = datetime.datetime.strptime(dob, "%d.%m.%Y")
			break
		except ValueError:
			print("Invalid date")

print(30 * "=")

# Printing todays day
today = datetime.datetime.now().date()
# taking birth date
birth_date = datetime.datetime.strptime(dob, "%d.%m.%Y").date()
# calculating 
age = today.year - birth_date.year - (
    (today.month, today.day) < (birth_date.month, birth_date.day)
)

# Appending to the list
inputs.append(age)

print(30 * "=")

# Generating unique ID with uuid
def short_uuid(i=8):
	return uuid.uuid4().hex[:i]

identifier = short_uuid(8).upper()

# append to the list
inputs.append(identifier)

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
	inputs.append(value)


# test
#print(select_list, type(select_list))


# convering it to dict to print it
select_list_dict = dict(select_list)


# appending country
inputs.append(select_list_dict["country"])

# printing date and time
today = datetime.datetime.now().strftime("%d.%m.%Y")

# appending date and time
inputs.append(today)



# printing ID issuing country
print(f"{select_list_dict['country']}\n {datetime.datetime.now().strftime('%d.%m.%Y')}")

print(inputs)
# Creating key list
keys = ["Name: ", "DOB: ", "Age: ", "ID No: ", "Address: ", "Issued by: ", "Country: ", "Lat: ", "Lon: ", "Issued by: ", "Date: "]


print(30 * "=")
print(30 * "=")

combined = dict(zip(keys, inputs))
print(combined)

for key, value in combined.items():
	n += 1
	print(f"{key}: {value}")






