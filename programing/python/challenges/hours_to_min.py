#===========================================================================#
# File: hours_to_min.py
# Author: Sava Maksimović
# Created: 8 June 2026
# Description: Takes an integer input representing total minutes.
# ## Converts the total minutes into hours and remaining minutes
# ## using arithmetic operators only.
# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#



# Arithmetic operators
# Convert minutes  and hours

# Takes the total minutes into hours and remaining minutes using arithmetic 
# operators only.

# setting up constant variable
HOUR = 60

user_input = int(input("Please input in minutes how much time you need for work: "))

# this is calculating one hour (60 minutes)
hour_calc = user_input // HOUR

# calculating what is left from user input
remaining_calc = (user_input - HOUR) % HOUR


# Printing all to the screen with f string
print(f"{hour_calc} hour(s) and {remaining_calc} minute(s)")







