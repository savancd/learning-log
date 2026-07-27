# importing library
import json
import time


# loading json file
with open("files/restaurant.json", "r", encoding="utf-8") as f:
	data = json.load(f)

if len(data["people"]) >= 8:
	print(f"Your group have more then 8 people: ")
	for keys in data["people"]:
		print(f"\t◾{keys['name']}")

	print(f"Waiting . . .")
	time.sleep(3)

else:
	print(f"Your group have less then 8 people!")

print(f"Your group table is ready!")



# print(data)
