import json


with open("files/rivers.json", "r", encoding="utf-8") as f:
	data = json.load(f)

print(type(data))


# It's gonna print all 
#for n in data:
#	print(n)

#print("=" * 30)


#for n in data:
	# to .get() must be inside "()" not inside "[]"
#	print(n.get("name"))


#(['name', 'location', 'flows', 'flowing_in', 'countries'])

# printing to check how many list of items ther is
#print(len(data))
# the type of .json data
#print(type(data))

for n in data:
	print(f'Each "n" is a type of {type(n)}{n["name"]}')

print("=" * 40)

for n in data:
	print(f"The {n["name"].title()} river is in the {n["location"].title()}")
	print(f"The river flows through: ")
	for e, i in enumerate(n["flows"]):
		e += 1
		print(f"\t{e}: {i.title()}")
	print(f"\tThe {n["name"].title()} is flowing into {n["flowing_in"].title()}.")
	print()
