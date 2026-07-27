user_age = int(input("What is your age?\n"))

if user_age <= 3:
	print("The ticket is free for kids under age of 3!")
elif user_age <= 12:
	print("The ticket is $10")
elif user_age > 12:
	print("The ticket is $15")
