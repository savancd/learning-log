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
	# taking date input  and breaking the loop if it's correct one
	try:
		date_of_birth = datetime.datetime.strptime(dob, "%d.%m.%Y")
		break
	# printing error onto screen if the format is not correct
	except ValueError:
		print("Incorect format. Please input it as is: DD.MM.YYYY")

print(30 * "=")

# Generating unique ID with uuid
def short_uuid(i=8):
	return uuid.uuid4().hex[:i]

identifier = short_uuid(8).upper()
print(f"ID No: {identifier}")

print(30 * "=")

# Asking user for their address

# Asking user to choose current address
print("Please choose  your current address!\n")

# pulling out places (cities) from a .json file
places = data.get("Places") or data.get("places") or []

# enumerating the list
for n, place in enumerate(places, 1):
	print(f"{n}. {place.get("city", "<unknown>")}")






