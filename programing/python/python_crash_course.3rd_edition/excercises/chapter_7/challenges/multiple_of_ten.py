user = int(input("Please Enter a number that is dividable by 10:\n"))

number = user


if user % 10 == 0:
	print(f"Your number is {user}, and it is a dividable by number 10")
	while number >= 0:
		print(f"\t◾Result: {number}")
		number = number - 10
		number = number

else:
	print("Your number is not dividable by 10!")
	while number >= 0:
		print(f"\t◾Result: {number}")
		number = number - 10
		number = number
