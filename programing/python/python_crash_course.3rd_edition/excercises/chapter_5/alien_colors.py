
# challenge alien_colors.py

# alien was just shot down in a game
# create a varieble with a _color name in it and assign the green, yellow or red.
# if statement should test which color is it and to print a message with points if
# the color is green
# if any other color except green, the program shoul fail, will not have points 

# importing library
import random
import inquirer

# making variable with) value green
color = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "lime", "teal"]
# randomising the choice of the color
random_color = random.choice(color)

# user input of the color
user_color = []

# points that user will get if correct answer
earned_points = 5
# starting points
points = 0

# printing current points
print(30 * "=")
print(f"Current amount of points: {points} ")
print(30 * "=")

# inquire list check of the options to choose from
questions = [
	inquirer.List(
		"colors",
		message="What color was the Alien?",
		choices=["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "white", "gray", "cyan", "magenta", "lime", "teal"],
	),
]

# taking inquire prompt to show on the screen
answers = inquirer.prompt(questions)
# taking prompt and assigning it to new variable names selected
selected = answers["colors"]


while True:
	# if the value is the same as  color it's gonna print extra points
	if selected == random_color:
		# calculating earned poits
		points += earned_points
		# printing it onto screen
		print(f"You earned {earned_points} points for correct answer!")

		# taking three time user input 
		for n in range(2): 
			# prnting a question to user
			print(f"Do you want to try one more time? (Yes/Y or No/N)\n")
			# taking user input and making it lower
			user_inp = input().lower()
			print(f"Current amount of points is: {points}\n")

			# checking is user entered corrent answer
			if user_inp == "yes" or user_inp == "y":
				answers = inquirer.prompt(questions)
				selected = answers["colors"]
				if selected == random_color:
					points += earned_points
					print(f"You have {points} points now.")
				else:
					print(f"Sorry, wrong answer.")
					break
			else:
				break
	else:
		print("Wrong answer.")
		print(30 * "=")
		print(f"The color was {random_color}")
		print(30 * "=")

		# priting a question to user
		print(f"Do you want to try one more time? (Yes/Y or No/N)\n")
		# taking user input and making it lower
		user_inp = input().lower()

		# checking is user entered corrent answer
		if user_inp == "yes" or user_inp == "y":
			answers = inquirer.prompt(questions)
			selected = answers["colors"]
			if selected == random_color:
				points += earned_points
				print(f"You have {points} points now.")
			else:
				print(f"Sorry, wrong answer.")
				break
		else:
			break

print(30 * "=")
print(f"The amount of points you got is: {points}")
print("Thank you for playing with us.")
print(30 * "=")



















