# importing library
import json

# loading the file
with open("guest_list.json", "r", encoding="utf-8") as f:
	data = json.load(f)

# checking data type
print(type(data))


print("These are keys: ")
for i, key in enumerate(data.keys()):
	print(f"{i}: {key}")

print("=" * 40)
print(data["event"])

# printing the event name to the screen
print(f"This is  data:  {data['event']['name']}")

print(data["event"]["date"].replace("_", "."))
