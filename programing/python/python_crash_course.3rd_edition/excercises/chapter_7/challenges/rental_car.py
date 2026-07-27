# Write a program that asks use what kind or rental car they would like, 
# print a message 

# Importing library
import json
import time

# opening the .json file with cars
with open("files/rental_car.json", "r", encoding="UTF8") as f:
	data = json.load(f)

# checking what type is the data
print(type(data))

# asking user which car he likes
user = input("Which car do you like the most?").lower().title()

# printing a message to the screen
print(f"Let me see if I can find you {user}!")
print(f"Thinking ...")

# pausing the python interpreter for the amount of seconds given
time.sleep(3)

# Checking if the user input exists in a list of cars
for c in data:
	if user  == c["car"]:
		print(f"We have {c['car']} with color {c['color']}\n")

# printing the message to the screen
print(f"We have only {len(data)} cars in out stock!\n")

# anumerating through the list from .json file
for i, k in enumerate(data):
	# enumerating each entry
	i += 1
	# printing all to the screen with every loop
	print(f"{i}: {k["car"].title()}, {k["color"].title()}")


