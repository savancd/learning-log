# importing library
import json

# loading the file
with open("guest_list.json", "r", encoding="utf-8") as f:
	data = json.load(f)

# checking data type
print(type(data))
#print(data)

print("These are keys: ")
for i, key in enumerate(data.keys()):
	print(f"{i}: {key}")

print("=" * 40)
print(data["event"])

# printing the event name to the screen
print(f"This is  data:  {data['event']['name']}")

print(data["event"]["date"].replace("_", "."))

# printing the keys from a .json
for key in data.keys():
	print(f"These are the keys: {key}")

# printing values from a dict
for i, item in enumerate(data["guest_list"]):
	print(f"This is the value {i}: {item}")

	# printing all the key and values from a list
	# to enumerate through both keys and values must enclose them inside ()
	for i, (key, values) in enumerate(item.items()):
		print(f"\t{i}: {key}: {values}")
	print()


#for i, n in data["guest_list"]:
