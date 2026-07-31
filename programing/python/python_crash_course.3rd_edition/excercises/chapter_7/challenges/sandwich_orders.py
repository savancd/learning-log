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

for o in orders["orders"]:
	print(f"I made your {o['name']}")

	num = 1
	n = num + 1

	new = {"id": n, "name": o }
	sandwiches.append(f"{new}, {o['name']}")

with open(path_sandwiches, "w", encoding="utf-8") as f:
	json.dump(sandwiches, f, indent=2)
