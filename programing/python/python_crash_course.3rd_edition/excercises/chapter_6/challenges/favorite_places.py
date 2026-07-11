
import json

with open("files/favorite_places.json", "r", encoding="utf-8") as f:
	data = json.load(f)

print(type(data))
print(data.keys())

#for v in data["favorite_places"]:

for v in data["favorite_places"]:
	for k, v in v.items():
		print(f"{k}'s favorite places are:")
		for v in v:
			print(f"\t◾{v}")
