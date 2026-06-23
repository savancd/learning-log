
import inquirer


print("Welcome to split bill calculator!")




while True:
	# checking is it a proper input
	try:
		bill_inp = int(input("What was total bill?\n"))
		break
	except ValueError:
		print(f"Please try again, enter only number!")

while True:
    try:
        people = int(input("How many people will split a bill?\n"))
        break
    except ValueError:
        print(f"Please try again, enter only number!")

while True:
	try:
		percentage = int(input("What is percentage amount you want to tip the waiter?\n"))
		break
	except ValueError:
		print("Enter a valid number!")


# to get percentage it should be divided by 100 to convert it to decimal
percent = percentage / 100

tip = bill_inp * percent
total = bill_inp + tip
# spliting total bill to the amount of people
split = total /  people

print(split)
