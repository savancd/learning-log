# Pizza challenge
# Think of at least three kind of your favirite pizza. 
# Store this names in a list
# Use a loop to print each name of pizza
# Modify your for loop to print a sentence using the name of the pizza,
# instead of printing just the name of the pizza. For each pizza, you should
# have one line of output containing a simple statement like I like pep-
#  peroni pizza.
# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence.





pizza = ["peperoni", "capricosa", "vojvodjanka"]


for n, name in enumerate(pizza):
	n += 1
	print(f"I love {name} pizza!")

print("I really like pizza")
