# importing library
import json

# loading the .json file
with open("files/cities.json", "r", encoding="utf-8") as f:
	data = json.load(f)


#print(data)

print("=" * 30)

# taking all from data and targeting cities
cities = data["cities"]


# looping through the list items
for name, i in cities.items():
	# printing the name of the city
	print(f"{name}")
	# looping through the list of items and getting all from the city names
	for n, c in i.items():
		# taking population key
		if n == "population":
			# converting it to string
			p_string = str(c)
			# reversing it so it can easier splitted properly
			rev = p_string[::-1]
			# spliting it into chunks of  3
			chunks = [rev[i:i+3] for i in range(0, len(rev), 3)]
			# formating it properly and reversing it again
			formated = ",".join(chunks)[::-1]
			# printing it properly formated
			print(f"\t{n.title()}: {formated}")
		else:
			print(f"\t{n.title()}: {c}")


#print(cities)

