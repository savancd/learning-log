


# Greetings
#  Start with a list from previous excercise. 
# Print a message to each person in the list
# Text each person from a list with a  unique message but the name must be specific person  name

names = ["Johny Depp", "Jack Black", "Nikola Tesla", "Selma Hayek", "Monika Beluchi"]


message = "you are invited to private party at my castle."

for num, name in enumerate(names):
	num += num
	print(f"{name}, {message}")
