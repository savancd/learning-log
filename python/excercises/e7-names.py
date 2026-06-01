

# Challenge names

# Store the names of a few of your friends in a list called names.
# Print each person name by accessing each element in the list. one at the time



names = ["Johny Depp", "Jack Black", "Nikola Tesla", "Selma Hayek", "Monika Beluchi"]


for num, name in enumerate(names):
	num = num + 1
	print(f"Person {num}: {name}")
