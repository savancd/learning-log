# Guest list
# Invite people to dinner, living or dead it doesnt matter.
# PList must include at learst three persons
# Prin a message to all people and invite them to dinner


# list of guests
guest_list = ["Nikola Tesla", "Jack Black", "Napoleon"]

# message for guests
message = "I would like to invite  "


for i, name in enumerate(guest_list):
	i = i + 1
	print(f"{i}: {message}{name} to my house for a dinner.")

cannot_come = "Unfortunatelly "
guest_not_comming = "Napoleon"

print(f"{cannot_come}{guest_not_comming} cannot come to the dinner, he is dead.")

# new guest invite replacing napoleon
guest_list[2] = "selma hayek"

#for i, name in enumerate(capitalized_names):
#	i = i + 1
#	print(f"Person {i}: {message}{name} to my house for a dinner")

print()
print()

print("I would like to inform that I find a bigger table for more guests and more space is available..")


guest_list.insert(0, "monica beluci")
guest_list.insert(2, "vlad cepesh")
guest_list.append("vlade divac")


capitalized_names = [name.title() for name in guest_list]


for num, name in enumerate(capitalized_names):
	num = num +1
	print(f"Person {num}: {message}{name} to my dinner party")


shrinking_list = "Unfortunatelly dinner table will not arrive on time for dinner, and now I have space only for two guests."

all_guests = list(guest_list)

print(shrinking_list)

for i, name in  enumerate(all_guests):
#	i = i + 1
	print(i, name)


print(f"I am sorry {all_guests.pop(1)} but I am unable to call you to dinner")
print(f"I am sorry {all_guests.pop(2)} but no comming for you to dinner")
print(f"I am sorry {all_guests.pop(3)} there is no space for you at dinner party")
print(f"Goodbye {all_guests.pop(1)} there is no space for all people at dinner")

print(all_guests, len(all_guests))

print(30 * "=")
print(30 * "=")

for num, name in enumerate(all_guests):
	num = num + 1
	print(f"{name.title()} you are invited to dinner party.")

























