# make a dict where each dict represent a different pet
# in each dict include what kind of animal and the owners name
# store dict in a list called pets
# loop through list and print all about pets

import json


with open("files/pets.json", "r", encoding="utf-8") as f:
	data = json.load(f)


#print(type(data))

for pet in data:
	for p in pet["pets"]:
		print(f'The pet is the "{p['pet'].title()}" and the owner is "{p['owner'].title()}"')
