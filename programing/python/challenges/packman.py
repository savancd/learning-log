#===========================================================================#
# File: packman.py
# Author: Sava Maksimović
# Created: 23 June 2026
# Description: Creating a maze using a list of strings, finding specific character 
# in a row, collumn ...
# Usage: Self Learning Challenge.
# License: MIT
# Notes:
# GitHub: https://github.com/savancd
#===========================================================================#
    


player = "P"
ghost = "G"
walls = "#"
pallets = "."

print(24 * walls)
print(walls,player,pallets * 16,ghost,walls)
print(walls,20 * pallets, walls)
print(24 * walls)

print(30 * "=")

# creating a maze list of objects
maze = [
	"######",
	"#P.G#",
	"#####"
]

print()
print(type(maze[0]))

# character that is to find
#char = "P"

char = ["P", "G"]

# checking how many rows there is
for i, n in enumerate(maze):
	print(f"Row number {i}: {n}")

print()
print(30 * "=")

dict_l = {}

# anumerating a list
for row_num, m in enumerate(maze):
	# checking and printing the characters and row
	if row_num == 1:
		count = len(m)
		print(f"Characters in row number {row_num}: {m}")

	# searching for specific character and finding his index number
	for chr in char:
		if str(chr) in m:
			# checking the index of character
			for i, ch in enumerate(chr):
				indx = m.index(chr)
				for c in ch:
					print(f"This is index: {indx} and the character {c}")
					dict_l[indx] = c



print(f"This is a index and a value {dict_l}\n{dict_l[1]}\n{dict_l[3]}")

