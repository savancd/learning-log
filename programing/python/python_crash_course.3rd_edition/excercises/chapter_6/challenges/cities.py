import json

with open("files/cities.json", "r", encoding="utf-8") as f:
	data = json.load(f)


#print(data)

print("=" * 30)

# checking what is the key
#for k in data.keys():
#	print(k)

# taking the data and extracting the cities
cities = data["cities"]

#print("=" * 30)



for key, country in cities.items():
	popul = country["population"]
	print(f"This is a original: {popul}")
	# converting it to str
	popul = str(popul)
	# reversing it
	rev = popul[::-1]
	print(f"Reversed 1: {rev}")

	#  spliting it every three char
	chunks = [rev[i:i+3] for i in range(0, len(rev), 3)]
	print(f"Splited: {chunks}")

	formatted = ",".join(chunks)[::-1]
	print(f"Formated for proper look: {formatted}")
	print("=" * 30)
	print(f"The city is {key} and the country is {country['country']}\n\tPopulation: {formatted}\n\tFact: {country['fact']}")
