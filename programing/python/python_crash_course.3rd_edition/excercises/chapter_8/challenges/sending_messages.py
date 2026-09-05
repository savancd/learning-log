import json

with open("files/messages.json", "r") as f:
	data = json.load(f)

print(type(data))

sent_messages = []

def send_messages(messages):
	for k, n in enumerate(messages):
		print(f"message: {n}")
		sent_messages.append(n)


message = data
send_messages(message)

print("#" * 40 )

# This is the sent message list
print("This is (sent_messages) list")
for k, n in enumerate(sent_messages):
	k += 1
	print(f"{k}: {n.title()}")
