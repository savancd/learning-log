#===========================================================================#
# File: shopping_list.py
# Author: Sava Maksimović
# Created: 9 June 2026
# Description: Instructions >>
##1. Create a shopping list
##2. Inside the file:
###- Create a list of at least 5 shopping items (import .json file)
###- Add new item
###- Remove existing item
###- Sort the list alphabeticaly
###- Print  a slice of the list (at least 3 items)
###- Display the final shopping list

# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#


# importing library
import json
import os
import sys


# importing and loading file into memory
with open("list.json", "r") as file:
	data = json.load(file)

# Test
#print(type(data))
#print(len(data["ShoppingList"]))

# enumerating list
for n, value in enumerate(data["ShoppingList"]):
	n += 1
	# printing each item on a separate line
	print(f"{n}: Item: {value['item']},\n   Quantity: {value['quantity']},\n   Unit: {value['unit'].title()},\n   Category: {value['category']}\n")


# Asking use does he/she wants to input new item to the list
while True:
	user_inp = input("Do you want to input new item to the list? (Yes/Y or No/N)\n").lower()
	if user_inp in ["yes", "y"]:
		# appending new item to the list
		# its just appending, not saving it
		data["ShoppingList"].append({
			"item": input("Item: "),
			"quantity": int(input("Quantity: ")),
			"unit": input("Unit: "),
			"category": input("Category: ")
		})

		# saving previous append to the list
		# overwriting the file with new items
		while True:
			user_q = input("Do you want to save into file new entry? Yes/y or No/n")
			if user_q.lower() == "yes":
				with open("list.json", "w") as f:
					json.dump(data, f, indent=4, ensure_ascii=False)
					break
			elif user_q.lower() == "y":
				with open("list.json", "w") as f:
					json.dump(data, f, indent=4, ensure_ascii=False)
					break
			else:
				print("Exiting...")
				break


		# printing new updated list
		for n, value in enumerate(data["ShoppingList"]):
			n += 1
			print(f"{n}: Item: {value['item']},\n   Quantity: {value['quantity']},\n   Unit: {value['unit'].title()},\n   Category: {value['category']}\n")
	else:
		break

print(len(data["ShoppingList"]))

# Asking user does he/she wants to remove some item
while True:
	user_inp = input("Do you want to remove some items from a list? (Yes/Y or No/N)\n ").lower()
	if user_inp == "yes" or user_inp == "y":
		try:
			user_num = int(input("Enter number of the items you want to remove!\n"))
		except ValueError:
			print("Please Enter a valid number input!\n")
			continue
		n = user_num - 1
		# removing item from user input
		item = data["ShoppingList"].pop(n)
		# printing it to the screen
		print(f"The item that will be removed is at nuber {user_num}: {item}")

		# overwriting the file 
		with open("list.json", "w") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
		# anumerating the list
		for n, value in enumerate(data["ShoppingList"]):
			n += 1
			# printing each item on a separate line
			print(f"{n}: Item: {value['item']},\n   Quantity: {value['quantity']},\nUnit: {value['unit'].title()},\n")

	else:
		# enumerating list
		for n, value in enumerate(data["ShoppingList"]):
			# printing each item on a separate line
			print(f"{n}: Item: {value['item']},\n   Quantity: {value['quantity']},\nUnit: {value['unit'].title()},\n")
			print("Exiting...")
			break
	# breaking the loop
	break



#for n in data["ShoppingList"]:
#	print(n.split())

#print(type(data["ShoppingList"]))
