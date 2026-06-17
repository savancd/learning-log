
# make a list with usernames, including the admin
# print a greeting to each person



# importing library
import json



# loading the .json file
with open("./files/users.json", "r") as file:
	data = json.load(file)

# printing the json file with 4 spaced indentation
#print(json.dumps(data, indent=4))


for n, name in enumerate(data):
	n += 1
	print(f"{n}: {name["name"]}")
	for movies in data:
		print(movies["known_movies"])
