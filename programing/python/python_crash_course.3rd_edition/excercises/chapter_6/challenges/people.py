# import library
import json

# list of people who should take a languages poll
poll_people = { 
	"people_for_poll": [
		{"name": "John Cusac", "email": "john@gmail.com", "gender": "m", "poll": "yes"},
		{"name": "Sharon Stone", "email": "ss@yahoo.com", "gender": "f", "poll": "yes"}
	]
}

# loading json file
with open("files/people_list.json", "r", encoding="utf-8") as f:
	data = json.load(f)

# printing to test the type of the data in a lists
print(f"Data .json file: {type(data)}\nPoll people dict: {type(poll_people)}\n","=" * 40)

# setting up a key 
key = "people_for_poll"

# looping through list and getting a key
for people in poll_people[key]:
	# key is made to be able to print the name of the list without {}
	print(f'There is {people['name'].title()} in a "{key}" list.',)

print("=" * 40)

for name in data["list_of_users"]:
	print(name)

print("=" * 40)

names_in_poll = (people["name"] for people in poll_people[key])

for user in data["list_of_users"]:
	if user["name"] in names_in_poll:
		print(f"There is {user["name"]} in a poll")
	else:
		print(f"There is no {user}")

#for name in data["list_of_users"]:
#	for people in poll_people[key]:
#		if name["name"] == people["name"]:
#			print("There is no same one")
#		else:
#			print(f"{name["name"]}")

print("=" * 40)

for name in data["list_of_users"]:
	if name["poll"] == "yes":
		# taking the full name of user and spliting it to print only a name
		name_spt = name["name"].split()
		if  name["gender"] == "f":
			print(f"Dear Ms. {name_spt[0]}. Thank you for taking the poll.")
		else:
			print("Hello Sir, {name_spt[0]}. Thank you for your time")
	else:
		print(f'{name["name"]}. Please take a poll')















