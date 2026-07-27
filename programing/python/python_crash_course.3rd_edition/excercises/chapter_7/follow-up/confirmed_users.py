# unconfirmed users
unconfirmed = ["alice", "brian", "candace"]
confirmed = []

# pop out the users from a list unconfirmed
while unconfirmed:
	current_user = unconfirmed.pop()
	# verifying users
	print(f"Verifying user {current_user.title()}")
	confirmed.append(current_user)

print(f"\nThe following users have been confirmed:")
for confirmed in confirmed:
	print(confirmed.title())
