#===========================================================================#
# File: body-mass-index.py
# Author: Sava Maksimović
# Created: 25 June 2026
# Description: Writting a program that calculate user's weight and height BMI
# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#

#import inquirer

print("**Welcome to the (BMI) Body Mass Index Calculator**")

#questions = [
#    inquirer.List(
#        "weight",
#        message="How do you want to enter your weight in??",
#        choices=["kg", "lbs"],
#    ),
#]

#answers = inquirer.prompt(questions)

#print(answers)

# looping until user enter properly
while True:
	print("Choose how you want you weight to enter:\n")
	# geting input from user, answers and making it lower case
	answers = input(f'"kg" or "lbs"') .lower()

	while True:
		# if the user enter specific "kg" or "lbs" its gonna skip to next or continue 
		if answers == "kg":
			user_weight = input("Please Enter you weight in kg:\n")

			try:
				# checking and validating is user entered properly as a integer
				weight = int(user_weight)
				break
			# if the user did not enter properly its gonna print next
			except ValueError:
				print("Please Enter only numbers!")

		elif answers == "lbs":
			user_weight = input("Enter your weight in lbs:\n")

			try:
				# must be float for lbs
				weight = float(user_weight)
				weight = weight * 703
				break
			except ValueError:
				print("Enter only numbers, no text!")

	# braking the loop to continue to next after everything is entered  by user
	break

while True:

#=================================================================================
# These parts are commented out for reason if the user enters weight
# in kg he/she will be prompted to enter height in specific height as cm or feet
#
#	print("How do you want to enter your height?\n")
#	answer = input('Choose 1 or 2:\n"1: cm"\n"2: feet"')

	# checking is user enter properly a number
#	try:
#		answer = int(answer)
#	except ValueError:
#		print('Enter only "1" or "2"')
#=======================================================

	if answers == "kg":
		user_height = input("Please Enter your height in cm:\n")
		try:
			height = int(user_height)
			# converting input from user to be in cm not in meters
			height = height / 100
			# calculating the bmi from user inputs
			bmi_kg = weight / height ** 2
			# rounding a  number to one decimal
			print(round(bmi_kg, 1))
			break
		except ValueError:
			print("Enter only numbers, no text!")

	elif answers == "lbs":
		user_height = input("Enter your height in feet:\n")
		try:
			# checking and converting user input to float
			height = float(user_height)
			# calculating inches from feet
			inches = height * 12
			# calculatin bmi, the inches must be squared as well
			bmi_in = weight / (inches ** 2)
			print(round(bmi_in, 1))
			break
		except ValueError:
			print("Enter only numbers not a text!")

print('Thank you for participating and trying our "BMI" calculator ')
