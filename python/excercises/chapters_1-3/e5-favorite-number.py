# Favorite number
# Use variable to represaent your favorite number. Then, using that variable, create a message that reveals 
# your favirite nuber. Print that message.


print("Please Enter your favorite number:")
num = int(input("\n"))


print(f"Your favorite number is: {num}")

if num % 2 == 0:
	print(f"Your number {num} is even.")
else:
	print(f"Your number {num} is odd.")
