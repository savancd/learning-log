# Make a list containing a series of short text messages.
# pass the list to function called show_messages()

# importing library
import json

# importing json file
with open("files/messages.json", "r") as f:
	data = json.load(f)

print(type(data))

# defining the function 
def show_messages(message):
	for k, n in enumerate(message):
		k += 1
		print(f"Message {k}: {n.title()}")

# getting data from json
message = data
# printing it to the screen
show_messages(message)
