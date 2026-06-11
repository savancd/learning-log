#===========================================================================#
# File: Favorite Movies List.py
# Author: Sava Maksimović
# Created: 9 June 2026
# Description: Instructions >>
##1. Create a file
##2. Inside the file:
###- Create a list of at least 5 favorite movies (import .json file)
###- Print the first movie
###- Print the last movie
###- Replace one movie with a new one
###- Print the updated list
###- Let the user choose an index and display the movie at that position

# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#

# importing library
import json
import os
import sys
import inquirer

# importing json file at the start of program
with open("movies.json", "r") as file:
	data = json.load(file)
# when importing from a .json, the data is dict

print(f"This is unchanged original list:")
# Instead printing entire file, targeting just the Movies
for n, movie in enumerate(data["Movies"], start=1): # start 1 makes that list gonna start form 1 and not at 0
	print(f"{n}: {movie}")

print(30 * "=")

# Printing first movie in the list
print(f"This is the FIRST movie in the list: {data["Movies"][1]}")

# Printing last movie in the list
print(f"This is the LAST movie in the list: {data["Movies"][-1]}")

print(30 * "=")

# replacing one movie name with a new value
data["Movies"][1] = "NO MOVIE ON THE LIST - This is a changed!"

print("This is updated list:")
# printing updated list with changed item
for name in data["Movies"]:
	print(f"{name}")

print(30 * "=")

# creating new list from a movie list
movie_list = []

for movie in data["Movies"]:
	# appending it to the new list
	movie_list.append(movie)

# Asking user to choose and print a movie
#print(type(movie_list))

questions = [
	inquirer.List(
		"Movie",
		message="Select and choose the movie to watch!",
		choices=movie_list,
	),
]
# the prompter that allow user to pick a movie from a list
# This is updated list
answers = inquirer.prompt(questions)

print(f"Today I want to watch {answers["Movie"]}")



# check data type
#print(type(movie))
