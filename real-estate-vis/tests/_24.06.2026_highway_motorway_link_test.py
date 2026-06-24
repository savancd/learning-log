import json

with open("/data/repo-learning/computer-Science-and-Software-Engineering/real-estate-vis/datasets/raw/2026/overpass-turbo/data/24.06.2026/highway_motorway_link.geojson", "r", encoding="utf-8") as file:
	data = json.load(file)


print(data.keys())

print(data["type"])
print(data["FeatureCollection"])


#print(data["type"]["properties"])
