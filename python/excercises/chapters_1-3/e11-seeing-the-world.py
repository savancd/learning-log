# Seeing the World
# Think of at least five places in the world that you would like to visit
# Store locationsin a list, 
# Print a list in a original order
# use sorted()
# show that a list is still in its original order by printing it
# use sorted() to print a list in a reverse alphbetical order without chaging the order 
# of original list
# user reverse() to change the order of a list again
# use sort() to change a list so it's stored in a reverse alphabetical order





# making a list of places
places = ["Moskva", "Seul", "Tokio", "Kyoto", "Singapore"]

# Original list order

print("This is a original order of the list:")
for num, city in enumerate(places):
	num += 1
	print(f"{num}: {city}")


print(30 * "=")

# Using sorted with a list
# Sorted returns a new sorted list without original list being changed
sorted_list = sorted(places)

print("This is a sorted order of the list:")
for num, name in enumerate(sorted_list):
	num += 1
	print(f"{num}: {name}")


print(30 * "=")


print("This is a original order of the list:")
# Still there is a original unchanged list
for num, city in enumerate(places):
	num += 1
	print(f"{num}:  {city}")


print(30 * "=")

# This is reversed sorted list
places.sort(reverse=True)
print("This is reversed sorted list: ")
for num, name in enumerate(places):
	num += 1
	print(f"{num}: {name}")



print(30 * "=")


# This is reversed list
places.reverse()
print("This is reversed  list: ")
for num, name in enumerate(places):
	num += 1
	print(f"{num}: {name}")




