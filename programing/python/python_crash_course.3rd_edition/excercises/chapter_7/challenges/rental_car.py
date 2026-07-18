# Write a program that asks use what kind or rental car they would like, 
# print a message 

import json

with open("files/rental_car.json", "r", encoding="UTF8") as f:
	data = json.load(f)


user = input("Which car you like the most?")

for k in data:
	for 
	print(f"{k['car']}")
