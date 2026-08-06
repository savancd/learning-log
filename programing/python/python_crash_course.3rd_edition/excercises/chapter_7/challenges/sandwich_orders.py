# sandwich_orders.py

import json

with open("files/sandwich_orders.json", "r", encoding="utf-8") as f:
	orders = json.load(f)

path_sandwiches = "files/finished_sandwiches.json"

with open("files/finished_sandwiches.json", "r", encoding="utf-8") as f:
	sandwiches = json.load(f)

#for n in orders:
	#k += 1
#	print(n)

# Printing orders list
name = orders["orders"]
print("Orders:\n")
for n, k in enumerate(name):
	n += 1
	# if there is a Pastrami in the order its gonna print it three times
	past = "Pastrami"
	if k["name"] == past:
		for k in range(3):
			print(f"{n}: {past}")
			n += 1
	else:
		print(f"{n}: {k["name"]}")

print("#" * 30)

# how many pastramis there is left
pastrami = 1
order_num = 1

# orders starting from 0 and increasing later 
order = 0

for o in orders["orders"]:
	# while true its gonna loop through list
	while True:
		# if the name si same to the Pastrami and if its equal to 0 its gonna print this if statement
		if o["name"] == "Pastrami" and pastrami == 0:
			print("Deli has run out of Pastrami")
		# its gonna print the list as well pastrami if previous one is not equal to 0
		else:
			if o["name"] == "Pastrami":
				print(f"I made your {o["name"]}\n" * 3)

				for _ in range(3):
#					print(o["id"])
					# creating new copy from o to be counted by one up
					new_o = o.copy()
					new_o["id"] += _

					new = {"order_num": order, "name": new_o}
					sandwiches.append(new)
			else:
				print(f"I made your {o['name']}")

				n += 1

				new = {"order_num": order, "name": o }
				sandwiches.append(new)

		break

# with every entry its gonna increase ID of the order
for id in sandwiches:
	if id["order_num"] == id["order_num"]:
		with open(path_sandwiches, "w", encoding="utf-8") as f:
			json.dump(sandwiches, f, indent=2)
		id["order_num"] += 1
	else:
		with open(path_sandwiches, "w", encoding="utf-8") as f:
			json.dump(sandwiches, f, indent=2)

#for id in sandwiches:
#	print(id)







