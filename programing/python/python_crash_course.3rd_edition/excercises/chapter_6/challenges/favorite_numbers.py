# challenge from section 6 automate with python book
# favorite number
# use a dictionary to store people favorite numbers
# minimum five names
# they should have a name, value, ...


# importing json
import json

# opening the file and reading it
with open("files/favorite_numbers.json", "r", encoding="utf-8") as f:
	data = json.load(f)


print(type(data))
print(data)

print("=" * 30)

print(data.keys())
print(data["persons"])

print("=" * 30)

# from data  pulling persons 
for i in data["persons"]:
	# if user is male in gender then will print it
	if i["gender"] == "m":
		print(f"{i["name"]} have his favorite number, that is {i["number"]}")
	# else if the user in gender is female, it's gonna print next line
	else:
		print(f"{i["name"]} have her favorite number, that is {i["number"]}")

print("=" * 30)

persons = data["persons"]

for n in persons:
	keys = n.keys()
	print(keys)

print("=" * 30)

# taking data from "persons"
for n in data["persons"]:
	# placing it into variable and getting a "name"
	name = n["name"]
	print(name)
