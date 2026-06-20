

current_users = ["miki_m", "eve_admin", "john_doe", "maya_k", "alex_lee", "omar_khan"]
new_users = ["sara_park", "tom_smith", "omar_khan", "eve_admin", "nina_ray"]

set_current = set(current_users)
set_new = set(new_users)




while True:
	user_input = input("Please enter your name:\n")
	user_inp = user_input.lower()


	for name in set_new:
		if name in current_users:
			print(f"{name} is in both lists")
		else:
			print(f"{name} is not in both list")

	if user_inp in set_current and user_inp in set_new:
		print(f"{user_inp} cannot be the same as existing ones.")
		print(f"You want to try one more time? (Yes/Y or No/N)")

		user_inputs = input("").lower()

		if user_inputs == "yes" or user_inputs == "y":
			user_input = input("Please enter your name:\n")
			user_inp = user_input.lower()
			print(f"The new user is: {user_inp}")
			break
	else:
		print(f"{user_inp} is available.")





