#===========================================================================#
# File: string_manipulation.py
# Author: Sava Maksimović
# Created: 8 June 2026
# Description: String manipulation, reverse name, count length, output initials
# Usage: Self Learning Challenge.
# License: MIT
# Notes: 
# GitHub: https://github.com/savancd
#===========================================================================#


# Taking input from a user
user_name_inp = input("Please Enter your full name:\n")

# reversing all the characters of the name
reversed_name = user_name_inp[::-1]

# spliting words into a list
split_first = reversed_name.split()

# separator on the screen
print(30* "=")

# Taking all first char of every word/name
first_char = [char[0] for char in split_first]

# calculating how many characters there is
calc = len(reversed_name)

# Number of characters in name
print(f"Number of characters in name: {calc}")

# Printing reversed name with uppercase first letter
print(reversed_name.title())

# Printing initials
print(f"These are initials: {"".join(first_char).upper()}")

