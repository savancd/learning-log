# import library
import json
import os

#current = os.getcwd()
#print(current)

# loading json file
with open("files/names.json", "r") as f:
	data = json.load(f)
print(type(data))

# defining the function  with parameter "names"
def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)

# creating empty list
username = []

# appending it to the empty list and extracting names
for name in data:
	username.append(name["name"])

# printing all to the screen and adding names from new created list with extracted names
greet_users(username)
