# Challenge learning Python
# Favorite book collector

# The  empty list
books = []


# Iterating 3 times to ask for three books names
for i in range(3):
	names = input("Please Enter your 3 favorite books: ")
	# Appending every book to the list
	books.append(names)
	# Iterating numbering
	i = i + 1

# Enuerating the printing
for n, name in enumerate(books):
	# Making it to start at 1 and not at 0
	n = n + 1
	# Printing everything to the screen 
	print(f"{n}: Your {n} book is name:  {name}")


# End message

print("Thank you for staying with me, working and learning with me!")
print("See you next time!")
