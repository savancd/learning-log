# looping until true
while True:
	# printing a message to the user
	print("Please enter the toping you want to put on pizza:")
	# when the user enters required word or letter it's gonna break the loop
	print('Input a "quit or q" when you finish all the topings')
	# asking user for input
	user = input("#: ").lower()
	print("=" * 40)
	# if loop until user enter quit or q it's gonna loop and print a message to the screen
	if user == "quit" or user == "q":
		break
	else:
		print(f'We added "{user}" on top of Pizza!')
		print("=" * 40)
