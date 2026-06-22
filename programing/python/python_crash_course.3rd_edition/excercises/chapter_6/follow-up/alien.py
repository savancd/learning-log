
# simple dictionary


# dictionaries compared to a list must be with curly braces "{}"
alien = {"color": "green", "points": 5}


# adding position values inside dict
alien["x-position"] = 0
alien["y-position"] = 25

# this will print only the key, not the value
for n in alien:
	print(n)

print("")

# this one will target all the values in dict
# by giving in .values() and print n
for n in alien.values():
	print(n)

print()

print(alien)
print(alien["color"])
print(alien["points"])




